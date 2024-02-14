from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
class Specialization(models.Model):
   name=models.CharField(max_length=100)
   special_image=models.ImageField(upload_to='doctor/spatialization/image',default="")
class Doctor(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
   specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
   gender=models.CharField(max_length=100,default="")
   phone=models.CharField(max_length=100,default="")
   biography=models.CharField(max_length=100,default="")
   address=models.CharField(max_length=100,default="")
   city=models.CharField(max_length=100,default="")
   country=models.CharField(max_length=100,default="")
   state=models.CharField(max_length=100,default="")
   postal_code=models.CharField(max_length=100,default="")
   date_birth = models.DateField(max_length=100, default=False)
   price=models.CharField(max_length=100,default="")
   doc_image=models.ImageField(upload_to='doctor/profile/img', default="")
   status = models.CharField(max_length=20, default='inactive', choices=(('active', 'Active'), ('inactive', 'Inactive')))
class Clinic(models.Model):
   doctor = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
   clinic_name=models.CharField(max_length=100,default="")
   clinic_image=models.ImageField(upload_to='doctor/clinics/img', default="")
   clinic_address=models.CharField(max_length=100,default="")

class Experience(models.Model):
   doctor = models.ForeignKey(User, on_delete=models.CASCADE)
   hospital_name=models.CharField(max_length=100,default="")
   designation=models.CharField(max_length=100,default="")
   start_date=models.DateField()
   end_date=models.DateField()
class Services(models.Model):
   doctor = models.ForeignKey(User, on_delete=models.CASCADE)
   service=models.CharField(max_length=100,default="")

class Degrees(models.Model):
   doctor = models.ForeignKey(User, on_delete=models.CASCADE)
   degree=models.CharField(max_length=100,default="")
   institute=models.CharField(max_length=100,default="")
   year=models.CharField(max_length=100,default="")
   
class Award(models.Model):
   doctor = models.ForeignKey(User, on_delete=models.CASCADE)
   awards=models.CharField(max_length=100,default="")
   award_year=models.CharField(max_length=100,default="")

class Patient(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
   date_birth=models.DateField(max_length=100,default=None)
   blood_group=models.CharField(max_length=100,default="")
   address=models.CharField(max_length=100,default="")
   city=models.CharField(max_length=100,default="")
   country=models.CharField(max_length=100,default="")
   state=models.CharField(max_length=100,default="")
   postal_code=models.CharField(max_length=100,default="")
   phone=models.CharField(max_length=100,default="")
   gender=models.CharField(max_length=100,default="")
   patient_image=models.ImageField(upload_to='patient/profile/img', default="")

class Subadmin(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
   date_birth=models.DateField(max_length=100,default=None)
   blood_group=models.CharField(max_length=100,default="")
   address=models.CharField(max_length=100,default="")
   city=models.CharField(max_length=100,default="")
   country=models.CharField(max_length=100,default="")
   state=models.CharField(max_length=100,default="")
   postal_code=models.CharField(max_length=100,default="")
   phone=models.CharField(max_length=100,default="")
   gender=models.CharField(max_length=100,default="")
   admin_image=models.ImageField(upload_to='admin/profile/img', default="")
  

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)   
    booking_date = models.DateField()
    appt_date = models.DateField()
    appt_time = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=(('New', 'New'), ('Accepted', 'Accepted'),('Confirmed','Confirmed'), ('Rejected', 'Rejected')), default='New')

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    day_of_week = models.CharField(max_length=20)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)

class Payment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)   
    payment_date = models.DateTimeField()
    amount=models.CharField(max_length=100,default="")
    status = models.CharField(max_length=20, default='Paid')
class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)   
    date = models.DateTimeField()
    message=models.TextField(max_length=1000,default="")
    title=models.CharField(max_length=250,default="")
    rating = models.PositiveIntegerField(default=0)

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} - {self.timestamp}'
class Contact(models.Model):
   name=models.CharField(max_length=100,default="")
   email=models.EmailField(max_length=100,default="")
   message=models.TextField(max_length=1000,default="")
   date=models.DateTimeField(auto_now_add=True)