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
  phone_number = models.CharField(max_length=14,blank=True)
  faculty = models.CharField(max_length=40,blank=True,null=True)
  major = models.CharField(max_length=40, blank=True)
  minor = models.CharField(max_length=40, blank=True)
  interests = models.CharField(max_length=200, blank=True)

  isExec = models.BooleanField()
  execPosition = models.CharField(max_length=40,blank=True,null=True)
  photo = models.ImageField(upload_to="chapter_roll/")

  def __unicode__(self):
    return self.name

  class Meta:
    ordering=['name']




