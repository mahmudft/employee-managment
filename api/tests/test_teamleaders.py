from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import TeamLeader, WorkTime

router = Client()


class TeamLeaderTestCase(TestCase):
    # client = APIClient()

    def setUp(self):
        print("Setting Up: Injecting test data for TeamLeader Test Case")
        WorkTime.objects.create(type="full-time", hours=30)
        hours = WorkTime.objects.get(hours=30)
        self.hours = hours
        TeamLeader.objects.create(team_leader_name="Leom", hourly_rate=20, worktime=self.hours)
        self.teamleader = TeamLeader.objects.get(team_leader_name="Leom")

    def test_post_teamleader_route(self):
        response = router.post(reverse('teamleader'), data={"team_leader_name": "Snapsis", "hourly_rate": 20, "worktime": self.hours.id}, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teamleader_route(self):
        response = router.get(reverse('teamleader'))
        print(response.data)
        self.assertEqual(len(response.data), 1)

    def test_put_teamleader_route(self):
        response = router.put(
            '/teamleader/{uid}'.format(uid=self.teamleader.id), data={"hourly_rate": 27}, content_type='application/json')
        print(response.data)
        self.assertEqual(response.data.get("total_rate"), 27 * 1.1)

    def test_delete_teamleader_route(self):
        response = router.delete(
            '/teamleader/{uid}'.format(uid=self.teamleader.id), content_type='application/json')
        print(response.data)
        self.assertEqual(response.data, [])
