from dataclasses import fields
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from api.models import Team, Employee, TeamLeader, WorkTime






class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = '__all__'
        

class TeamLeaderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    total_rate = serializers.SerializerMethodField(
        method_name="recalculate_hourly_field")
    worktime = WorkTimeSerializer(required=False, allow_null=True)

    def recalculate_hourly_field(self, obj):
        return obj.hourly_rate * 1.1

    class Meta:
        model = TeamLeader
        fields = '__all__'
    
    def recalculate_hourly_field(self, object):
        return object.hourly_rate * 1.1
        

class TeamSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    team_leader = TeamLeaderSerializer(required=False, allow_null=True)

    class Meta:
        model = Team
        depth = 1
        fields = '__all__'
    

class EmployeeSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    team = TeamSerializer(required=False, allow_null=True)
    worktime = WorkTimeSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
