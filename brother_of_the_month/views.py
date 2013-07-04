# Create your views here.

from models import botm_entry
from django.template import RequestContext
from django.shortcuts import render_to_response


def brother_of_the_month(request):
	botm_entries = botm_entry.objects.all()
	context = RequestContext(request,{'botm_entries' : botm_entries})
	return render_to_response('brother_of_the_month.html', context)
