from django.forms import ModelForm
from django.contrib.auth.views import get_user_model
from django import forms

from .models import Profile, GENDERS

User = get_user_model()


class ProfileForm(ModelForm):
    gender = forms.ChoiceField(required=False, choices=GENDERS)
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'gender', 'bio']


class UserForm(ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

