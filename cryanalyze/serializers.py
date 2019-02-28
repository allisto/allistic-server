from rest_framework import serializers

from .models import BigData, SmallData


class BigDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigData
        fields = ('parameter',)


class SmallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallData
        fields = ('parameter',)
