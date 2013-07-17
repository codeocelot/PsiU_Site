from django.db import models

class carouselImage(models.Model):
	image = models.ImageField(upload_to="carousel")
	caption = models.CharField(max_length=200)

	def image_thumb(self):
    return '<img src="/media/%s" width="100" height="100" />' % (self.photo)

  image_thumb.allow_tags = True