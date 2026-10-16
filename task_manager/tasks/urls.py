from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    TaskMetricsView,
    TaskPerformanceReportView,
    ProjectListCreateView,
    ProjectDetailView,
    TagListCreateView,
    TagDetailView,
    NotificationListView,
    NotificationMarkReadView,
    UserListView,
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/metrics/', TaskMetricsView.as_view(), name='task-metrics'),
    path('analytics/performance-report/', TaskPerformanceReportView.as_view(), name='task-performance-report'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/read/', NotificationMarkReadView.as_view(), name='notification-mark-read'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]


