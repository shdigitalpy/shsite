from django.shortcuts import render
from django.core.mail import send_mail
from .models import Sender

def index(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_surname = request.POST['surname']
		message_email = request.POST['email']
		message_url = request.POST['url']
		message_body = request.POST['message']

		send_mail(
    		'Ihre Antwort - ' + message_name + ' ' + message_surname,
    		message_body,
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

		return render(request, 'index.html', {'message_surname': message_surname})

	else: 
		return render(request, 'index.html', {})

def kennzahlen(request):
	page_bc = 'Online Kennzahlen'
	context = {'page_bc':page_bc}
	return render(request, 'blog/online-kennzahlen.html', context)

def digital_marketing_strategien(request):
	page_bc = 'Digital Marketing Strategien'
	context = {'page_bc':page_bc}
	return render(request, 'blog/digital-marketing-strategien.html', context)

def wer_wir_sind(request):
	page_bc = 'Wer wir sind'
	context = {'page_bc':page_bc}
	return render(request, 'blog/wer-wir-sind.html', context)