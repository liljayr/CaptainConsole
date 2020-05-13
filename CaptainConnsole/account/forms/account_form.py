from django.forms import ModelForm, widgets
from django import forms

from account.models import User, ProfileImage


class EditAccountForm(ModelForm):
   # image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'groups', 'user_permissions']
        widgets = {
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class EditImageForm(ModelForm):
    class Meta:
        model = ProfileImage
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }