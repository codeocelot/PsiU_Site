from django.db import models

class botm_entry(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="images/")
  image_caption = models.CharField(max_length=1000,blank=True)

  MONTH = (('JAN','January'),
  	('FEB','February'),
  	('MAR','March'),
  	('APR','April'),
  	('MAY','May'),
  	('JUN','June'),
  	('JUL','July'),
  	('AUG','August'),
  	('SEPT','September'),
  	('OCT','October'),
  	('NOV','November'),
  	('DEC','December'))

  month = models.CharField(choices=MONTH, max_length=10)

  description = models.TextField(max_length=100000)

  year_of_initiation = models.CharField(max_length=4)
  year_of_graduation = models.CharField(max_length=4)

  major = models.CharField(max_length=50)
  
