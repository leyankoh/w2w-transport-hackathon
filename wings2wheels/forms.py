from django import forms
from .models import UserForm
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


GENDER_CHOICES = [('female', 'Female'),
                  ('male', 'Male')]

class User(ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = UserForm
        fields = ['name','gender', 'email', 'phone_number', 'flight_number', 'date', 'time',"mode"]
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
