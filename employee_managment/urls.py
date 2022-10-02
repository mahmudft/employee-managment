from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ApiRoot, employee_view, employee_view_detail, teamleader_view, teamleader_view_detail, teams_view, team_view_detail, worktime_view, worktime_view_detail
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('teams/', teams_view, name="teams"),
    path('teams/<int:pk>', team_view_detail),
    path('worktime/', worktime_view, name="worktime"),
    path('worktime/<int:pk>', worktime_view_detail),
    path('teamleader/', teamleader_view, name="teamleader"),
    path('teamleader/<int:pk>', teamleader_view_detail),
    path('employees/', employee_view, name="employees"),
    path('employees/<int:pk>', employee_view_detail),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('swagger/', schema_view.with_ui('swagger',
                                                cache_timeout=0), name="swagger-schema")
]
