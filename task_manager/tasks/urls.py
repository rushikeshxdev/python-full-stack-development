from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    TaskMetricsView,
    ProjectListCreateView,
    ProjectDetailView,
    TagListCreateView,
    TagDetailView,
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/metrics/', TaskMetricsView.as_view(), name='task-metrics'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]

