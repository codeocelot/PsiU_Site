from django.contrib import admin
from brother_of_the_month.models import botm_entry

class botm_entryAdmin(admin.ModelAdmin):
	list_display = ('name','month')
admin.site.register(botm_entry, botm_entryAdmin)