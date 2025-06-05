"""
URL configuration for hashout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Import this!
from django.conf import settings  # Import settings (for DEBUG check)
from django.conf.urls.static import (
    static,
)  # Import static (for serving other static in dev)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pwa.urls")),
    # --- PWA Specific URL patterns for root files ---
    path(
        "sw.js",
        TemplateView.as_view(
            template_name="sw.js", content_type="application/x-javascript"
        ),
    ),
    path(
        "manifest.json",
        TemplateView.as_view(
            template_name="manifest.json", content_type="application/json"
        ),
    ),
    # --- End PWA Specific URL patterns ---
]

# This line is crucial for Django to serve static files (like your icons) during development
# Do NOT use this in production.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # The above `static` helper is for serving files found by `collectstatic`.
    # For files in `STATICFILES_DIRS` (like your `static/images/`),
    # `django.contrib.staticfiles` (which is in INSTALLED_APPS) handles it automatically in DEBUG mode.
