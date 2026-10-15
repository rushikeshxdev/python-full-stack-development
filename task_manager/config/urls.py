from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.utils import extend_schema
from rest_framework.throttling import ScopedRateThrottle
from tasks.views import RegisterView, HealthCheckView
from tasks.serializers import CustomTokenObtainPairSerializer


@extend_schema(tags=['Authentication'], summary='Obtain JWT access & refresh token pair (Login)')
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'auth'



@extend_schema(tags=['Authentication'], summary='Refresh JWT access token')
class RefreshView(TokenRefreshView):
    pass


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('api/v1/health/', HealthCheckView.as_view(), name='api-health-check'),
    path('api/v1/auth/register/', RegisterView.as_view(), name='register'),
    path('api/v1/auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('tasks.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

