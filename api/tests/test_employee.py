from unicodedata import name
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Employee, Team, TeamLeader, WorkTime

router = Client()


class EmployeesTestCase(TestCase):
    # client = APIClient()

    def setUp(self):
        print("Setting Up: Injecting test data for Employees Test Case")
        WorkTime.objects.create(type="full-time", hours=30)
        hours = WorkTime.objects.get(hours=30)
        TeamLeader.objects.create(team_leader_name="Micheal", hourly_rate=10, worktime=hours)
        TeamLeader.objects.create(
            team_leader_name="Adam", hourly_rate=10, worktime=hours)
        leader = TeamLeader.objects.get(team_leader_name="Adam")
        self.teamleader = leader
        self.team = Team.objects.create(
            team_name="Communication", team_leader=TeamLeader.objects.get(team_leader_name="Micheal"))
        self.hours = WorkTime.objects.get(hours=30)
        Employee.objects.create(name="Zdan", team=self.team, hourly_rate=10, worktime=hours)
        self.employee = Employee.objects.get(name="Zdan")

    def test_post_employees_route(self):
        response = router.post(reverse('employees'), data={"name": "Caroline", "team": self.team.id, "hourly_rate": 10, "worktime": self.hours.id}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employees_route(self):
        response = router.get(reverse('employees'))
        self.assertEqual(len(response.data), 1)

    def test_put_employees_route(self):
        response = router.put(
            '/employees/{uid}'.format(uid=self.employee.id), data={"name": "Jenny"}, content_type='application/json')
        self.assertEqual(response.data.get("name"), "Jenny")

    def test_delete_employees_route(self):
        response = router.delete(
            '/employees/{uid}'.format(uid=self.employee.id), content_type='application/json')
        self.assertEqual(response.data, [])
