"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls',namespace='auth')),
    path('', include('ml_app.urls', namespace='ml_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
