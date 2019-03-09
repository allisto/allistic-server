from django.contrib import admin

from .models import SmallData, BigData, CryAudio

admin.site.register(SmallData)
admin.site.register(BigData)
admin.site.register(CryAudio)
