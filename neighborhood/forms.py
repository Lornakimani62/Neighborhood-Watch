from .models import *
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['name']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['id']

class NotifyForm(forms.ModelForm):
    class Meta:
        model=Notification
        exclude=['post_date']