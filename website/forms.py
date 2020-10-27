from django import forms
from .models import Sender
from bootstrap_modal_forms.forms import BSModalModelForm

FORMCHOICES = [
	('Choice 1', 'Bitte kontaktieren Sie mich für ein kostenloses Strategiegespräch'), 
	('Choice 2', 'Setzen Sie mich auf die Warteliste')
	]

class SenderModelForm(BSModalModelForm):
    class Meta:
        model = Sender
        fields = ['message_name', 'message_surname', 'message_email', 'message_phone', 'message_body']
        labels = {
        	'message_name' : '',
        	'message_surname' : '',
        	'message_email' : '',
        	'message_phone' : '',
        	'message_body' : '',

        }
        widgets = {
        	'message_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihr Vorname'}),
        	'message_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre Nachname'}),
        	'message_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre E-Mail Adresse'}),
        	'message_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihre Telefon'}),
        	'message_body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ihr Kommentar bezüglich unserer Kontaktaufnahme'}),
        }