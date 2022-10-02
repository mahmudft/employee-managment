from rest_framework import routers

from api.views import TeamViewSet

router = routers.DefaultRouter

router.register('/team', TeamViewSet)