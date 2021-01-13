from django.shortcuts import render
from django.core.mail import send_mail
from .models import Sender
from .forms import SenderModelForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from datetime import datetime
from django.contrib import messages



def index(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_surname = request.POST['surname']
		message_email = request.POST['email']
		message_url = request.POST['url']
		message_body = request.POST['message']

		send_mail(
    		'Ihre Antwort - ' + message_name + ' ' + message_surname,
    		message_surname + ' ' + message_name + ' möchte eine 24 Stunden Analyse.' + ' Folgende Nachricht wurde hinterlassen:' + message_body + ' ' + 'Die Url lautet: ' + message_url,
    		message_email,
    		['sandro@sh-digital.ch'],
    		fail_silently=False,
			)

		if Sender.objects.filter(message_email=message_email).exists():
			t = Sender.objects.get(message_email=message_email)
			t.message_body = message_body
			t.save()

		else: 
			t = Sender(message_name=message_name, message_surname=message_surname, message_email=message_email, message_url=message_url, message_body=message_body)
			t.save()

		x = datetime.now()
		today = x.strftime('%m' + '.' + '%Y')

		context = {
			'today': today,
			'message_surname': message_surname,
			'success_message': success_message

		 }
		 

		success_message = 'Die Nachricht wurde gesendet!'
		return render(request, 'index.html',context)

	else:
		x = datetime.now()
		today = x.strftime('%m' + '.' + '%Y')
		context = {
			'today': today,

		 }
		return render(request, 'index.html', context)

def web_design(request):
	context = { }
	return render(request, 'web-design.html', context)

def web_entwicklung(request):
	context = { }
	return render(request, 'web-entwicklung.html', context)

def seo(request):
	context = { }
	return render(request, 'seo.html', context)

def google_ads(request):
	context = { }
	return render(request, 'google-ads.html', context)

def facebook_ads(request):
	context = { }
	return render(request, 'facebook-ads.html', context)

def coaching(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_surname = request.POST['surname']
		message_email = request.POST['email']
		message_url = request.POST['url']
		message_body = request.POST['message']

		send_mail(
    		'Ihre Antwort - ' + message_name + ' ' + message_surname,
    		message_surname + ' ' + message_name + ' möchte eine 24 Stunden Analyse.' + ' Folgende Nachricht wurde hinterlassen:' + message_body + ' ' + 'Die Url lautet: ' + message_url,
    		message_email,
    		['sandro@sh-digital.ch'],
    		fail_silently=False,
			)

		if Sender.objects.filter(message_email=message_email).exists():
			t = Sender.objects.get(message_email=message_email)
			t.message_body = message_body
			t.save()

		else: 
			t = Sender(message_name=message_name, message_surname=message_surname, message_email=message_email, message_url=message_url, message_body=message_body)
			t.save()

		success_message = 'Die Nachricht wurde gesendet!'
		return render(request, 'index.html', {'message_surname': message_surname, 'success_message': success_message})

	else: 
		return render(request, 'coaching.html', {})


def kennzahlen(request):
	page_bc = 'Online Kennzahlen'
	page_k = 'Online Kennzahlen für Kleinunternehmer, Selbständige und Startups'
	context = {'page_bc':page_bc, 'page_k': page_k}
	return render(request, 'blog/online-kennzahlen.html', context)

def digital_marketing_strategien(request):
	page_bc = 'Digital Marketing Strategien'
	context = {'page_bc':page_bc}
	return render(request, 'blog/digital-marketing-strategien.html', context)

def wer_wir_sind(request):
	page_bc = 'Wer wir sind'
	context = {'page_bc':page_bc}
	return render(request, 'blog/wer-wir-sind.html', context)

def ueber_uns(request):
	context = {}
	return render (request, 'ueber-uns.html', context)

class SenderCreateView(BSModalCreateView):
	template_name = 'send-modal.html'
	form_class = SenderModelForm
	success_message = 'Die Anfrage wurde gesendet!'
	success_url = reverse_lazy('index')



	