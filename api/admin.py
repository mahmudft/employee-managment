from django.contrib import admin

from api.models import Employee, Team, TeamLeader, WorkTime

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


class TeamLeaderAdmin(admin.ModelAdmin):
    pass


class WorkTimeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TeamLeader, TeamLeaderAdmin)
admin.site.register(WorkTime, WorkTimeAdmin)
