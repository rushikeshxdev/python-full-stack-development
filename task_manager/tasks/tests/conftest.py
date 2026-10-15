import pytest
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from tasks.models import Task, Project, Tag
from tasks.constants import TaskStatus, TaskPriority


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def rbac_groups(db):
    admin_grp, _ = Group.objects.get_or_create(name='Admin')
    contrib_grp, _ = Group.objects.get_or_create(name='Contributor')
    viewer_grp, _ = Group.objects.get_or_create(name='Viewer')
    return {
        'admin': admin_grp,
        'contributor': contrib_grp,
        'viewer': viewer_grp,
    }


@pytest.fixture
def admin_user(db, rbac_groups):
    user = User.objects.create_user(username='fixture_admin', password='Password123!', is_staff=True)
    user.groups.add(rbac_groups['admin'])
    return user


@pytest.fixture
def contributor_user(db, rbac_groups):
    user = User.objects.create_user(username='fixture_contrib', password='Password123!')
    user.groups.add(rbac_groups['contributor'])
    return user


@pytest.fixture
def viewer_user(db, rbac_groups):
    user = User.objects.create_user(username='fixture_viewer', password='Password123!')
    user.groups.add(rbac_groups['viewer'])
    return user


@pytest.fixture
def auth_client_factory(api_client):
    def _create_auth_client(user):
        client = APIClient()
        client.force_authenticate(user=user)
        return client
    return _create_auth_client


@pytest.fixture
def sample_project(db, contributor_user):
    return Project.objects.create(
        name='Test Fixture Project',
        description='Project for testing',
        owner=contributor_user
    )


@pytest.fixture
def sample_tags(db):
    tag1 = Tag.objects.create(name='backend')
    tag2 = Tag.objects.create(name='frontend')
    tag3 = Tag.objects.create(name='devops')
    return [tag1, tag2, tag3]


@pytest.fixture
def bulk_tasks(db, contributor_user, sample_project, sample_tags):
    tasks = []
    for i in range(15):
        task = Task.objects.create(
            title=f"Task #{i+1}",
            description=f"Generated task description {i+1}",
            status=TaskStatus.TODO if i % 2 == 0 else TaskStatus.IN_PROGRESS,
            priority=TaskPriority.HIGH if i % 3 == 0 else TaskPriority.MEDIUM,
            owner=contributor_user,
            project=sample_project
        )
        task.tags.set(sample_tags[:2])
        tasks.append(task)
    return tasks
