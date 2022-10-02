from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import WorkTime

router = Client()


class WorkTimeTest(TestCase):
    # client = APIClient()

    def setUp(self):
        response = router.post(reverse('worktime'), data={
            "type": "part-time", "hours": 12}, format='json')
        self.id = response.data["id"]
        print("Setting Up: Injecting test data")
        pass

    def test_post_new_work_schedule(self):
        response = router.post(reverse('worktime'), data={
                               "type": "part-time", "hours": 22}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_work_schedules(self):
        response = router.get(reverse('worktime'))
        self.assertEqual(len(response.data), 1)

    def test_put_work_schedule(self):
        response = router.put(
            '/worktime/{uid}'.format(uid=self.id), data={"hours": 27}, content_type='application/json')
        self.assertEqual(response.data.get("hours"), 27)

    def test_delete_work_schedule(self):
        response = router.delete(
            '/worktime/{uid}'.format(uid=self.id), content_type='application/json')
        self.assertEqual(response.data, [])
