import pytest
from rest_framework import status
from tasks.models import Task
from tasks.constants import TaskStatus


@pytest.mark.django_db
@pytest.mark.parametrize("role_fixture, expected_status", [
    ("viewer_user", status.HTTP_403_FORBIDDEN),
    ("contributor_user", status.HTTP_201_CREATED),
    ("admin_user", status.HTTP_201_CREATED),
])
def test_task_creation_role_matrix(request, auth_client_factory, role_fixture, expected_status, sample_project):
    user = request.getfixturevalue(role_fixture)
    client = auth_client_factory(user)

    payload = {
        "title": f"Matrix Task by {user.username}",
        "description": "Role matrix validation",
        "status": TaskStatus.TODO,
        "project": sample_project.id,
    }
    response = client.post('/api/v1/tasks/', payload, format='json')
    assert response.status_code == expected_status


@pytest.mark.django_db
@pytest.mark.parametrize("role_fixture, expected_status", [
    ("viewer_user", status.HTTP_403_FORBIDDEN),
    ("contributor_user", status.HTTP_403_FORBIDDEN),
    ("admin_user", status.HTTP_204_NO_CONTENT),
])
def test_task_deletion_role_matrix(request, auth_client_factory, role_fixture, expected_status, contributor_user, sample_project):
    """
    Validates that:
    - Viewers cannot delete (403)
    - Contributors cannot delete ANY task, even their own (403)
    - Admins can delete any task (204)
    """
    task = Task.objects.create(
        title="Deletion Candidate Task",
        status=TaskStatus.TODO,
        owner=contributor_user,
        project=sample_project
    )

    user = request.getfixturevalue(role_fixture)
    client = auth_client_factory(user)

    response = client.delete(f'/api/v1/tasks/{task.id}/')
    assert response.status_code == expected_status
    if expected_status == status.HTTP_204_NO_CONTENT:
        assert not Task.objects.filter(id=task.id).exists()
    else:
        assert Task.objects.filter(id=task.id).exists()


@pytest.mark.django_db
def test_contributor_cannot_modify_other_user_task(auth_client_factory, contributor_user, admin_user, sample_project):
    # Task owned by admin
    admin_task = Task.objects.create(
        title="Admin Task",
        owner=admin_user,
        project=sample_project
    )

    contrib_client = auth_client_factory(contributor_user)
    response = contrib_client.patch(f'/api/v1/tasks/{admin_task.id}/', {"title": "Hacked Title"}, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_contributor_can_modify_own_task(auth_client_factory, contributor_user, sample_project):
    own_task = Task.objects.create(
        title="Own Task",
        owner=contributor_user,
        project=sample_project
    )

    contrib_client = auth_client_factory(contributor_user)
    response = contrib_client.patch(f'/api/v1/tasks/{own_task.id}/', {"title": "Updated by Owner"}, format='json')
    assert response.status_code == status.HTTP_200_OK
    own_task.refresh_from_db()
    assert own_task.title == "Updated by Owner"
