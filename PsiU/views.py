from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from carousel.models import carouselImage

def landing_page(request):
	Images = carouselImage.objects.all()
	context = RequestContext(request,{"Images" : Images})
	return render_to_response('index.html',context)

# def about(request):
# 	return render(request,'about.html')

def calendar(request):
	return render(request, 'calendar.html')

def rush(request):
	return render(request, 'rush.html')

def contact_us(request):
	return render(request, 'contact_us.html')

def phil(request):
  return render(request,'phil.html')

def house(request):
  return render(request,'house.html')

def international(request):
  return render(request,'international.html')

def chapter(request):
  return render(request,'chapter.html')

def news(request):
    return render(request,'news.html')

def scholar(request):
    return render(request,'scholar.html')

def movember(request):
    return redirect('http://moteam.co/psi-upsilon')

