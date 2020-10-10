from django.shortcuts import render
from django.core.mail import send_mail
from .models import Sender

def index(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_surname = request.POST['surname']
		message_email = request.POST['email']
		message_phone = request.POST['phone']
		message_body = request.POST['message']

		send_mail(
    		'Ihre Antwort - ' + message_name + message_surname,
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
			t = Sender(message_name=message_name, message_surname=message_surname, message_email=message_email, message_phone=message_phone, message_body=message_body)
			t.save()

		return render(request, 'index.html', {'message_surname': message_surname})

	else: 
		return render(request, 'index.html', {})

def kennzahlen(request):
	return render(request, 'blog/online-kennzahlen.html', {})