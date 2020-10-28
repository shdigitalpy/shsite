from django import forms
from .models import Sender
from bootstrap_modal_forms.forms import BSModalModelForm

class SenderModelForm(BSModalModelForm):
    class Meta:
        model = Sender
        fields = ['message_surname','message_name', 'message_email', 'message_phone', 'message_body']
        widgets = {
        	'message_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihr Vorname'}),
        	'message_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre Nachname'}),
        	'message_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre E-Mail Adresse'}),
        	'message_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre Telefon'}),
        	'message_body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wann sind Sie telefonisch am besten erreichbar'}),
        }