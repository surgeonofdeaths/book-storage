from django.forms import ModelForm
from django.contrib.auth.views import get_user_model
from django import forms

from .models import Profile, GENDERS

User = get_user_model()


class ProfileForm(ModelForm):
    gender = forms.ChoiceField(choices=GENDERS)
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['gender', 'avatar', 'bio']


class UserForm(ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
