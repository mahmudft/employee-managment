from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Team, TeamLeader, WorkTime

router = Client()

def request_teams_endpoint():
    response = router.post(reverse('worktime'), data={
        "type": "part-time", "hours": 22}, content_type='application/json')
    return response

class TeamsTestCase(TestCase):
    # client = APIClient()

    def setUp(self):
        print("Setting Up: Injecting test data for TeamLeader Test CAse")
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

    def test_post_teams_route(self):
        response = router.post(reverse('teams'), data={
                               "team_name": "Marketing", "team_leader": self.teamleader.id}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teams_endpoint(self):
        response = router.get(reverse('teams'))
  
        self.assertGreater(len(response.data), 0)

    def test_put_teams_endpoint(self):
        response = router.put(
            '/teams/{uid}'.format(uid=self.team.id), data={"team_name": "Communication2"}, content_type='application/json')
        self.assertEqual(response.data.get("team_name"), "Communication2")

    def test_delete_teams_endpoint(self):
        response = router.delete(
            '/worktime/{uid}'.format(uid=self.team.id), content_type='application/json')
        self.assertEqual(response.data, [])
