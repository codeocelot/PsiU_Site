from django.shortcuts import render, render_to_response
from django.template import RequestContext
from chapter_roll.models import brother

def chapter_roll(request):
	brothers = brother.objects.all()
	context = RequestContext(request,{"brothers":brothers})
	return render_to_response('chapter_roll.html',context)
