from rest_framework import serializers

from .models import BigData, SmallData, CryAudio


class CryAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryAudio
        fields = (
            'audio_file',
        )


class BigDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigData
        fields = (
            'zcr', 'energy', 'entropy_energy', 'spectral_spread_1', 'spectral_spread_2', 'spectral_entropy',
            'spectral_flux_1',
            'spectral_flux_2', 'spectral_rolloff', 'mfcc_1', 'mfcc_2', 'mfcc_3', 'mfcc_4', 'mfcc_5', 'mfcc_6', 'mfcc_7',
            'mfcc_8', 'mfcc_9', 'mfcc_10', 'mfcc_11', 'label')


class SmallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallData
        fields = ('class_type', 'id', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11',
                  'm12', 'm13', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'fft1', 'fft2',
                  'fft3', 'fft4', 'fft5', 'fft6', 'fft7', 'fft8', 'fft9', 'fft10', 'fft11', 'fft12',
                  'fft13', 'fft14', 'fft15', 'fft16', 'fft17', 'fft18', 'fft19', 'fft20', 'fft21', 'fft22',
                  'fft23', 'fft24', 'fft25', 'fft26', 'fft27', 'fft28', 'fft29', 'fft30', 'fft31', 'fft32',
                  'fft33', 'fft34', 'fft35', 'fft36', 'fft37', 'fft38', 'fft39', 'fft40', 'fft41', 'fft42',
                  'fft43', 'fft44', 'fft45', 'fft46', 'fft47', 'fft48', 'fft49', 'fft50', 'fft51', 'fft52',
                  'fft53', 'fft54', 'fft55', 'fft56', 'fft57', 'fft58', 'fft59', 'fft60', 'fft61', 'fft62',
                  'fft63', 'fft64',)
