from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

class Doctor(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
   gender=models.CharField(max_length=100,default="")
   phone=models.CharField(max_length=100,default="")
   date_birth=models.DateTimeField(default="")
   biography=models.CharField(max_length=100,default="")
   address=models.CharField(max_length=100,default="")
   city=models.CharField(max_length=100,default="")
   country=models.CharField(max_length=100,default="")
   state=models.CharField(max_length=100,default="")
   postal_code=models.CharField(max_length=100,default="")
   price=models.CharField(max_length=100,default="")
   doc_image=models.ImageField(upload_to='doctor/profile/img', default="")
class Award(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   clinic_name=models.CharField(max_length=100,default="")
   clinic_image=models.ImageField(upload_to='doctor/clinics/img', default="")
   clinic_address=models.CharField(max_length=100,default="")
class Specialization(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   specialization=models.CharField(max_length=100)
class Experience(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   hopital_name=models.CharField(max_length=100,default="")
   designation=models.CharField(max_length=100,default="")
   start_date=models.DateField()
   end_date=models.DateField()
class Services(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   service=models.CharField(max_length=100,default="")

class Degrees(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   degree=models.CharField(max_length=100,default="")
   institute=models.CharField(max_length=100,default="")
   year=models.CharField(max_length=100,default="")
   
class Award(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   awards=models.CharField(max_length=100,default="")
   award_year=models.CharField(max_length=100,default="")

class Patient(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
   date_birth=models.DateField(default="")
   blood_group=models.CharField(max_length=100,default="")
   address=models.CharField(max_length=100,default="")
   city=models.CharField(max_length=100,default="")
   country=models.CharField(max_length=100,default="")
   state=models.CharField(max_length=100,default="")
   postal_code=models.CharField(max_length=100,default="")
   price=models.CharField(max_length=100,default="")
   phone=models.CharField(max_length=100,default="")

  

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)   
    booking_date = models.DateField()
    appt_date = models.DateField()
    appt_time = models.TimeField()

    def __str__(self):
        return f'{self.doctor} - {self.patient} - {self.date} {self.time}'
    

class AppointmentStatus(models.Model):
    APPOINTMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    appointment = models.ForeignKey(Appointment, related_name='appointment_status', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(User, related_name='doctor_schedule', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
