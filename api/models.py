from unicodedata import name
from django.db import models

# Create your models here.


class WorkTime(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(help_text="Work type either full-time or part-time", max_length=15)
    hours = models.IntegerField(help_text="hours per week full-time 40hrs/week")

    def __str__(self) -> str:
        return self.type


class TeamLeader(models.Model):
    id = models.AutoField(primary_key=True)
    team_leader_name = models.CharField(max_length=50)
    hourly_rate = models.IntegerField(default=0)
    worktime = models.ForeignKey(WorkTime, blank=True, null=True,  on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.team_leader_name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50)
    team_leader = models.OneToOneField(TeamLeader, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.team_name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    team = models.ForeignKey(Team, null=True, default=None ,on_delete=models.SET_NULL)
    hourly_rate = models.IntegerField()
    worktime = models.ForeignKey(WorkTime, null=True,  on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
