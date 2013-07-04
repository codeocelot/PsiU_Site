from django.db import models

from django.db import models

class carouselImage(models.Model):
  image = models.ImageField(upload_to="carousel")
  caption = models.CharField(max_length=200)

