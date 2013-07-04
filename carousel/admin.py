from django.contrib import admin
from .models import carouselImage

class carouselImageAdmin(admin.ModelAdmin):
    list_display=('image','caption')
    
admin.site.register(carouselImage,carouselImageAdmin)
