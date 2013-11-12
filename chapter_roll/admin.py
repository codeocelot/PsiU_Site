from django.contrib import admin
from chapter_roll.models import brother

class brotherAdmin(admin.ModelAdmin):
	list_display = ('name','year_joined')
admin.site.register(brother,brotherAdmin)
