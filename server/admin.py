from django.contrib import admin
from .models import Doctor, ConsultationTime, Medicine, Allergy, Child, Parent
# Register your models here.

admin.site.register(Doctor)
admin.site.register(ConsultationTime)
admin.site.register(Medicine)
admin.site.register(Allergy)
admin.site.register(Child)
admin.site.register(Parent)