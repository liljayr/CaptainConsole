from django.forms import ModelForm, widgets
from account.models import Location, CardInfo


class CheckoutAddressForm(ModelForm):
    class Meta:
        model = Location
        exclude = ['id', 'user']
        widgets ={
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'streetname': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_nr': widgets.NumberInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'})
        }

class CheckoutCardForm(ModelForm):
     class Meta:
         model = CardInfo
         exclude = ['id']
         widgets ={
             'card_holder':widgets.TextInput(attrs={'class':'form-control'}),
             'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
             'Exp_date': widgets.DateInput(attrs={'class': 'form-control'}),
             'CVC': widgets.NumberInput(attrs={'class': 'form-control'})
         }
