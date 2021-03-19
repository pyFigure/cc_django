"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static
{%- if cookiecutter.use_swagger.lower() == 'y' %}
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from OpenAPI.swager import CustomOpenAPISchemaGenerator


schema_view = get_schema_view(
    openapi.Info(
        title="infra OPEN api",
        default_version='v1.0.0',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomOpenAPISchemaGenerator
)
{%- endif %}

# 系统及第三方依赖路由
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    {%- if cookiecutter.use_mdeditor.lower() == 'y' %}
    path('mdeditor/', include('mdeditor.urls')),
    {%- endif %}
    {%- if cookiecutter.use_sphinx.lower() == 'y' %}
    path('docs/', include('docs.urls')),
    {%- endif %}
    path('admin/', admin.site.urls)
]

# 自研 APP 路由
urlpatterns += [
    path('<version>/account/', include('account.urls')),
    {%- if cookiecutter.use_demo.lower() == 'y' %}
    path('demo/<version>/', include('demo.urls')),
    {%- endif %}
]

{%- if cookiecutter.use_swagger.lower() == 'y' %}
# api & doc
urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
{%- endif %}


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
