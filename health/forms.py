from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('status', 'user', 'dob', 'doj')





















        


# This is a Django form class named DoctorForm which inherits from forms.ModelForm. It is used to define a 
# form for creating or updating instances of the Doctor model.
# The Meta class inside the DoctorForm defines the model to which the form is related to, and specifies 
# any additional metadata required. In this case, the Doctor model is set as the model for the form, and 
# two fields status, user, dob and doj are excluded from the form.
# The exclude attribute tells Django to exclude these fields from the form, which means they will not be 
# included in the HTML form and will not be submitted when the form is saved.
# This form can be used in a view to display a form to create or update a doctor instance in the database