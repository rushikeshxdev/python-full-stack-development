"""
Central URL Configuration for task_manager.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # Modern Web UI (Single Page Application)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    path('admin/', admin.site.urls),

    # Version 1 API (Industry Best Practice)
    path('api/v1/', include('tasks.urls')),

    # Backwards-compatible /api/ alias
    path('api/', include('tasks.urls')),

    # OpenAPI 3.0 / Swagger Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
