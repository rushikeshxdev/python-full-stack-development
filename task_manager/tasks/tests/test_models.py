import pytest
from tasks.models import Task, Project, Tag
from tasks.constants import TaskStatus, TaskPriority


@pytest.mark.django_db
def test_task_model_string_representation(contributor_user):
    task = Task.objects.create(
        title="Check String Rep",
        owner=contributor_user
    )
    assert str(task) == "[TODO] Check String Rep"


@pytest.mark.django_db
def test_project_model_string_representation(contributor_user):
    project = Project.objects.create(
        name="Apollo Mission",
        owner=contributor_user
    )
    assert str(project) == "Apollo Mission"


@pytest.mark.django_db
def test_tag_model_string_representation():
    tag = Tag.objects.create(name="devops")
    assert str(tag) == "#devops"


@pytest.mark.django_db
def test_task_default_values(contributor_user):
    task = Task.objects.create(
        title="Default Check Task",
        owner=contributor_user
    )
    assert task.status == TaskStatus.TODO
    assert task.priority == TaskPriority.MEDIUM
    assert task.created_at is not None
    assert task.updated_at is not None
