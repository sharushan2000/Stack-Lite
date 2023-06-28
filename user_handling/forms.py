from stackapp.models import UserProfile,Ticket,Comment
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name' ,'last_name','username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio','pic','github','public')


