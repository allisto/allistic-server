from rest_framework import viewsets

from .models import (
    BigData,
    SmallData,
)
from .serializers import BigDataSerializer, SmallDataSerializer


class BigDataViewset(viewsets.ModelViewSet):
    queryset = BigData.objects.all()
    serializer_class = BigDataSerializer


class SmallDataViewset(viewsets.ModelViewSet):
    queryset = SmallData.objects.all()
    serializer_class = SmallDataSerializer
