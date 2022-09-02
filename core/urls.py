"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from news_parser import views

from rest_framework.schemas import get_schema_view

app_name = 'core'

schema_url_patterns = [
    path('api/v1/', include('news_parser.urls')),
]


urlpatterns = [
    path('', views.links, name='links'),
    path('admin/', admin.site.urls),
    path('logout/', RedirectView.as_view(url='/admin/logout/')),

    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'openapi-schema'},
    ), name="docs"),

    path('openapi/', get_schema_view(
        title="News service",
        description="API",
        version="1.0.0",
        patterns=schema_url_patterns,
    ), name='openapi-schema'),

    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include('news_parser.urls')),
]