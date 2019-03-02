from rest_framework import viewsets

from .models import (
    BigData,
    SmallData,
    CryAudio,
)
from .serializers import BigDataSerializer, SmallDataSerializer, CryAudioSerializer

"""
python code to post audio file
url = "http://localhost:8000/api/v1/audio/"
files = {'file': open('./sample_upload_audio.mp3', 'rb')}
r = requests.post(url, files=files)
"""


class CryAudioViewSet(viewsets.ModelViewSet):
    queryset = CryAudio.objects.all()
    serializer_class = CryAudioSerializer


class BigDataViewSet(viewsets.ModelViewSet):
    queryset = BigData.objects.all()
    serializer_class = BigDataSerializer


class SmallDataViewSet(viewsets.ModelViewSet):
    queryset = SmallData.objects.all()
    serializer_class = SmallDataSerializer
