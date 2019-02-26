from django.contrib import admin

from .models import Doctor, ConsultationTime, Medicine, Allergy, Child, Parent

admin.site.site_header = "Allisto - We Do Good"


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhar_number', 'specialization', 'email', 'phone_number')
    list_filter = ('specialization', 'consultation_fee', 'working_hours')
    search_fields = ('name', 'specialization', 'consultation_fee')


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhar_number', 'email', 'phone_number', 'address')
    list_filter = ('name', 'email', 'phone_number')
    search_fields = ('name', 'aadhar_number', 'email', 'phone_number', 'address')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'autistic', 'birthday', 'gender')
    list_filter = ('name', 'autistic', 'birthday')
    search_fields = ('name', 'autistic', 'birthday')


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name',)


admin.site.register(ConsultationTime)
