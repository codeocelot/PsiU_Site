from django.contrib import admin
from chapter_roll.models import brother

class brotherAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number')
admin.site.register(brother,brotherAdmin)