from rest_framework import routers

from cryanalyze import api_views

router = routers.DefaultRouter()
router.register(r'big-data', api_views.BigDataViewSet)
router.register(r'small-data', api_views.SmallDataViewSet)
router.register(r'audio', api_views.CryAudioViewSet)
