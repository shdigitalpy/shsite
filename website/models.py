from django.db import models

class Sender(models.Model):
	message_name = models.CharField(max_length=255)
	message_surname = models.CharField(max_length=255)
	message_email = models.EmailField(max_length=255, unique=True)
	message_phone = models.IntegerField()
	message_url = models.CharField(max_length=255, default='www')
	message_body = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.pk) + self.message_name
