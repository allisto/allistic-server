from rest_framework import routers

from cryanalyze import api_views

router = routers.DefaultRouter()
router.register(r'big-data', api_views.BigDataViewset)
router.register(r'small-data', api_views.SmallDataViewset)
