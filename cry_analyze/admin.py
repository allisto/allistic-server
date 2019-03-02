from django.contrib import admin

from .models import SmallData, BigData

admin.site.register(SmallData)
admin.site.register(BigData)
