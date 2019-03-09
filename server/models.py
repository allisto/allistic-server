from django.core.validators import RegexValidator
from django.db import models

WEEKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
]


class ConsultationTime(models.Model):
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()


class Medicine(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Allergy(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=30)
    aadhar_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not a Phone Number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    unique=True)  # validators should be a list
    address = models.CharField(max_length=100, null=True)

    def get_parent_name(self):
        return str(self.name)

    def get_parent_aadhar_number(self):
        return str(self.aadhar_number)

    def get_parent_email(self):
        return str(self.email)

    def get_parent_phone_number(self):
        return str(self.phone_number)

    def get_parent_address(self):
        return str(self.address)


class Doctor(models.Model):
    MD = "MD"
    MBBS = "MBBS"

    name = models.CharField(max_length=30)
    aadhar_number = models.CharField(max_length=12, unique=True)
    specialization = models.CharField(max_length=10, choices=(
        (MD, "Master In Doctor"),
        (MBBS, "MBBS"),
    ), default=MBBS)

    degree_proof = models.FileField()
    experience_years = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not a Phone Number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    unique=True)  # validators should be a list
    address = models.CharField(max_length=100)
    consultation_fee = models.IntegerField()
    working_hours = models.ManyToManyField(ConsultationTime)

    patient_list = models.ManyToManyField(Parent, related_name="treats")

    def get_doctor_name(self):
        return str(self.name)

    def get_doctor_aadhar_number(self):
        return str(self.aadhar_number)

    def get_doctor_email(self):
        return str(self.email)

    def get_doctor_specialization(self):
        return str(self.specialization)

    def get_doctor_exp_years(self):
        return self.experience_years

    def get_doctor_phone_number(self):
        return str(self.phone_number)

    def get_doctor_address(self):
        return str(self.address)

    def get_doctor_consultation_fees(self):
        return self.consultation_fee


class Child(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=30)
    autistic = models.NullBooleanField()
    birthday = models.DateField()
    aadhar_number = models.CharField(max_length=12, blank=True, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medicine_list = models.ManyToManyField(Medicine, related_name="takes")

    def __str__(self):
        return self.name
