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
    aadhar_number = models.CharField(max_length=12)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not a Phone Number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=100, null=True)


class Doctor(models.Model):
    MD = "MD"
    MBBS = "MBBS"

    name = models.CharField(max_length=30)
    aadhar_number = models.CharField(max_length=12)
    specialization = models.CharField(max_length=10, choices=(
        (MD, "Master In Doctor"),
        (MBBS, "MBBS"),
    ), default=MBBS)

    degree_proof = models.FileField()
    experience_years = models.IntegerField()
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not a Phone Number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=100)
    consultation_fee = models.IntegerField()
    working_hours = models.ManyToManyField(ConsultationTime)

    patient_list = models.ManyToManyField(Parent, related_name="treats")


class Child(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=30)
    autistic = models.NullBooleanField()
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medicine_list = models.ManyToManyField(Medicine, related_name="takes")

    def __str__(self):
        return self.name
