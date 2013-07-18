from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from carousel.models import carouselImage

def landing_page(request):
	Images = carouselImage.objects.all()
	context = RequestContext(request,{"Images" : Images})
	return render_to_response('index.html',context)

def about(request):
	return render(request,'about.html')

def calendar(request):
	return render(request, 'calendar.html')

def rush(request):
	return render(request, 'rush.html')

def contact_us(request):
	return render(request, 'contact_us.html')
