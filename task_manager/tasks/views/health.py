from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import connection
from django.core.cache import cache
from django.utils import timezone
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=['Health & Infrastructure'],
    summary='Liveness and Readiness probe for Load Balancers (ALB / Nginx)',
    description='Checks database and cache connectivity. Returns 200 OK if healthy, 503 if primary dependency is down.'
)
class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        health_status = {
            "status": "healthy",
            "timestamp": timezone.now().isoformat(),
            "services": {
                "database": "unknown",
                "cache": "unknown"
            }
        }
        status_code = status.HTTP_200_OK

        # 1. Check PostgreSQL Database
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if row and row[0] == 1:
                    health_status["services"]["database"] = "connected"
                else:
                    health_status["services"]["database"] = "degraded"
                    health_status["status"] = "unhealthy"
                    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        except Exception as e:
            health_status["services"]["database"] = f"error: {str(e)}"
            health_status["status"] = "unhealthy"
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE

        # 2. Check Redis Cache
        try:
            cache.set("healthcheck_probe", "ok", timeout=5)
            val = cache.get("healthcheck_probe")
            if val == "ok":
                health_status["services"]["cache"] = "connected"
            else:
                health_status["services"]["cache"] = "degraded"
        except Exception as e:
            health_status["services"]["cache"] = f"error: {str(e)}"

        return Response(health_status, status=status_code)
