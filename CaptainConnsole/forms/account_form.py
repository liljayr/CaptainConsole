from django.forms import ModelForm, widgets
from django import forms

from account.models import Accounts


class EditAccountForm(ModelForm):
    image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Accounts
        exclude = ['id', 'first_name', 'last_name', 'house_nr', 'city', 'country', 'password', 'postal_code',
                   'street_name', 'role']
        widgets = {
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }


