from django.forms import ModelForm, widgets
from account.models import Accounts

class ProfileForm(ModelForm):
    class Meta:
        model =   Accounts
        exclude = [ 'id' , 'user' ]

        widgets = {
           'username': widgets.TextInput(attrs={'class' : 'form-control'}),
           'email': widgets.TextInput(attrs={'class': 'form-control'})}
#                   'favorite_candy': widgets.Select(attrs={'class' : 'form-control'},
#                   'profile_image' : widgets.TextInput(attrs={'class' : 'form-control'}
#               }