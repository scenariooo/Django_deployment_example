from django import forms
from django.contrib.auth.models import User
from basic_app.models import userprofiles

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User

        fields = ('username','email','password')

class userprofilesinfo(forms.ModelForm):
    class Meta():
        model = userprofiles
        fields = ('portfolio_site','portfile_pic')        