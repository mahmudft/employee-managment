"""employee_managment URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ApiRoot, employee_view, employee_view_detail, teamleader_view, teamleader_view_detail, teams_view, team_view_detail, worktime_view, worktime_view_detail


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
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]
