from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Admin_Helath_CSV)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Search_Data)





















# This code registers the models Admin_Helath_CSV, Doctor, Patient, Feedback, and Search_Data to the 
# Django admin site, which allows for easy management of database entries through a web interface. 
# Once registered, these models can be viewed, edited, and deleted through the admin site.