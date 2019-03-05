# Generated by Django 2.0.8 on 2019-03-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zcr', models.DecimalField(decimal_places=4, max_digits=10)),
                ('energy', models.DecimalField(decimal_places=4, max_digits=10)),
                ('entropy_energy', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_spread_1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_spread_2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_entropy', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_flux_1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_flux_2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('spectral_rolloff', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_3', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_4', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_5', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_6', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_7', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_8', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_9', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_10', models.DecimalField(decimal_places=4, max_digits=10)),
                ('mfcc_11', models.DecimalField(decimal_places=4, max_digits=10)),
                ('label', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CryAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SmallData',
            fields=[
                ('class_type', models.CharField(choices=[('MR', 'MR'), ('ADULT', 'ADULT')], max_length=5)),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('m1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m3', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m4', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m5', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m6', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m7', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m8', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m9', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m10', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m11', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m12', models.DecimalField(decimal_places=4, max_digits=10)),
                ('m13', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l3', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l4', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l5', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l6', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l7', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l8', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l9', models.DecimalField(decimal_places=4, max_digits=10)),
                ('l10', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft1', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft3', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft4', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft5', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft6', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft7', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft8', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft9', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft10', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft11', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft12', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft13', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft14', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft15', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft16', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft17', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft18', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft19', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft20', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft21', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft22', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft23', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft24', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft25', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft26', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft27', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft28', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft29', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft30', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft31', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft32', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft33', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft34', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft35', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft36', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft37', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft38', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft39', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft40', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft41', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft42', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft43', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft44', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft45', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft46', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft47', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft48', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft49', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft50', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft51', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft52', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft53', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft54', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft55', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft56', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft57', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft58', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft59', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft60', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft61', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft62', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft63', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fft64', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
