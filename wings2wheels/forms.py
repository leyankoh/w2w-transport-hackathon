from django import forms
import datetime

class UserForm(forms.Form):
    """
    booking form to gather information about the passenger
    we will need to know:
    name
    gender

    phone number
    email
    flight number
    dates
    time

    PREFERENCES
    mode of transport
    single gender?
    allergies
    chatty?
    """
    GENDER_CHOICES = [('female', 'Female'),
                      ('male', 'Male')]

    name = forms.CharField(max_length=200)
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    flight_number = forms.CharField(max_length=10)
    date = forms.DateTimeField()


class PreferenceForm(forms.Form):
    