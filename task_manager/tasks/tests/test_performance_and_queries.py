import pytest
from rest_framework import status
from tasks.services import get_task_metrics


@pytest.mark.django_db
def test_task_list_query_count_scales_without_n_plus_one(django_assert_num_queries, auth_client_factory, contributor_user, bulk_tasks):
    """
    Regression Test:
    Ensures listing tasks scales with O(1) database queries regardless of result count.
    Boundary expected:
      - Query 1: Pagination COUNT(*)
      - Query 2: SELECT tasks with select_related('owner', 'assigned_to', 'project')
      - Query 3: SELECT tags with prefetch_related('tags')
    """
    client = auth_client_factory(contributor_user)

    with django_assert_num_queries(3):
        response = client.get('/api/v1/tasks/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 15
        assert len(response.data['results']) == 10  # PAGE_SIZE is 10


@pytest.mark.django_db
def test_task_metrics_executes_in_single_sql_query(django_assert_num_queries, bulk_tasks):
    """
    Regression Test:
    Ensures task metrics aggregation executes in a single SQL query via conditional COUNTs.
    """
    with django_assert_num_queries(1):
        metrics = get_task_metrics()
        assert metrics['total'] == 15
        assert metrics['todo'] > 0
        assert metrics['in_progress'] > 0


@pytest.mark.django_db
def test_projects_list_query_count(django_assert_num_queries, auth_client_factory, contributor_user, sample_project):
    """
    Regression Test:
    Ensures fetching project list executes in a single query.
    """
    client = auth_client_factory(contributor_user)
    with django_assert_num_queries(1):
        response = client.get('/api/v1/projects/')
        assert response.status_code == status.HTTP_200_OK
