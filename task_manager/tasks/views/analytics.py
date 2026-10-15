from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema

from ..serializers import TaskMetricsSerializer, TaskPerformanceReportSerializer
from ..services import get_task_metrics, get_heavy_performance_report


@extend_schema(
    tags=['Analytics & Metrics'],
    summary='Retrieve aggregated task statistics',
    responses={200: TaskMetricsSerializer}
)
class TaskMetricsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        metrics = get_task_metrics()
        return Response(metrics, status=status.HTTP_200_OK)


@extend_schema(
    tags=['Analytics & Metrics'],
    summary='Retrieve comprehensive system performance report (Heavy analytical computation)',
    responses={200: TaskPerformanceReportSerializer}
)
class TaskPerformanceReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        report = get_heavy_performance_report()
        return Response(report, status=status.HTTP_200_OK)

