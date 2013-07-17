from django.db import models
import datetime

# Create your models here.

class brother(models.Model):
	INIT_CHOICES = []
	for r in range(2005, (datetime.datetime.now().year+1)):
		INIT_CHOICES.append((r,r))

	GRAD_CHOICES = []
	for r in range((datetime.datetime.now().year), datetime.datetime.now().year+10):
		GRAD_CHOICES.append((r,r))


	name = models.CharField(max_length=100)
	year_joined = models.IntegerField(('Initiated'), max_length=4, choices=INIT_CHOICES, default=datetime.datetime.now().year)
	year_graduate = models.IntegerField(('Expected Graduation'), max_length=4, choices=GRAD_CHOICES, default=datetime.datetime.now().year)
	phone_number = models.CharField(max_length=14)
	faculty = models.CharField(max_length=40)
	major = models.CharField(max_length=40)
	minor = models.CharField(max_length=40)
	interests = models.CharField(max_length=200)

	photo = models.ImageField(upload_to="chapter_roll/")






