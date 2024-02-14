from django.contrib import admin
from .models import User,Doctor,Patient,Specialization,Services,Clinic,Experience,Degrees
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialization)
admin.site.register(Services)
admin.site.register(Clinic)
admin.site.register(Experience)
admin.site.register(Degrees)