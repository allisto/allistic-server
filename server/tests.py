import mock
from django.core.files import File
from django.test import TestCase

from server.models import Doctor, Parent

degree_proof = mock.MagicMock(spec=File)


class DoctorTestCase(TestCase):
    def setUp(self):
        Doctor.objects.create(name="Doctor 1",
                              aadhar_number="123456789123",
                              specialization="MD",
                              email="doctor1@gmail.com",
                              phone_number="9474556775",
                              address="Address 1",
                              consultation_fee=500,
                              experience_years=10)

        Doctor.objects.create(name="Doctor 2",
                              aadhar_number="234567891231",
                              specialization="MBBS",
                              email="doctor2@gmail.com",
                              phone_number="9474556774",
                              address="Address 2",
                              consultation_fee=300,
                              experience_years=12)

    def test_doctors_name(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_name(), 'Doctor 1')
        self.assertEqual(doctor2.get_doctor_name(), 'Doctor 2')

    def test_doctor_aadhar(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_aadhar_number(), '123456789123')
        self.assertEqual(doctor2.get_doctor_aadhar_number(), '234567891231')

    def test_doctor_specialization(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_specialization(), 'MD')
        self.assertEqual(doctor2.get_doctor_specialization(), 'MBBS')

    def test_doctor_email(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_email(), 'doctor1@gmail.com')
        self.assertEqual(doctor2.get_doctor_email(), 'doctor2@gmail.com')

    def test_doctor_phone_number(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_phone_number(), '9474556775')
        self.assertEqual(doctor2.get_doctor_phone_number(), '9474556774')

    def test_doctor_address(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_address(), 'Address 1')
        self.assertEqual(doctor2.get_doctor_address(), 'Address 2')

    def test_doctor_consultation_fee(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_consultation_fees(), 500)
        self.assertEqual(doctor2.get_doctor_consultation_fees(), 300)

    def test_doctor_experience(self):
        doctor1 = Doctor.objects.get(name="Doctor 1")
        doctor2 = Doctor.objects.get(name="Doctor 2")
        self.assertEqual(doctor1.get_doctor_exp_years(), 10)
        self.assertEqual(doctor2.get_doctor_exp_years(), 12)


class ParentTestCase(TestCase):

    def setUp(self):
        Parent.objects.create(
            name="Parent 1",
            aadhar_number="123456789123",
            email="parent1@gmail.com",
            phone_number="9474556774",
            address="Address1",
        )
        Parent.objects.create(
            name="Parent 2",
            aadhar_number="023456789123",
            email="parent2@gmail.com",
            phone_number="9474556775",
            address="Address2",
        )

    def test_parent_name(self):
        parent1 = Parent.objects.get(name="Parent 1")
        parent2 = Parent.objects.get(name="Parent 2")
        self.assertEqual(parent1.get_parent_name(), 'Parent 1')
        self.assertEqual(parent2.get_parent_name(), 'Parent 2')

    def test_parent_aadhar(self):
        parent1 = Parent.objects.get(name="Parent 1")
        parent2 = Parent.objects.get(name="Parent 2")
        self.assertEqual(parent1.get_parent_aadhar_number(), '123456789123')
        self.assertEqual(parent2.get_parent_aadhar_number(), '023456789123')

    def test_parent_email(self):
        parent1 = Parent.objects.get(name="Parent 1")
        parent2 = Parent.objects.get(name="Parent 2")
        self.assertEqual(parent1.get_parent_email(), 'parent1@gmail.com')
        self.assertEqual(parent2.get_parent_email(), 'parent2@gmail.com')

    def test_parent_phone_number(self):
        parent1 = Parent.objects.get(name="Parent 1")
        parent2 = Parent.objects.get(name="Parent 2")
        self.assertEqual(parent1.get_parent_phone_number(), '9474556774')
        self.assertEqual(parent2.get_parent_phone_number(), '9474556775')

    def test_parent_address(self):
        parent1 = Parent.objects.get(name="Parent 1")
        parent2 = Parent.objects.get(name="Parent 2")
        self.assertEqual(parent1.get_parent_address(), 'Address1')
        self.assertEqual(parent2.get_parent_address(), 'Address2')
