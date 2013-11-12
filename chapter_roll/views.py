from django.shortcuts import render, render_to_response
from django.template import RequestContext
from chapter_roll.models import brother

def chapter_roll(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q == "exec":
            brothers = brother.objects.filter(isExec=True)
            return render(request,'chapter_roll.html',{'brothers':brothers, "section":"Executive"})
    else:
        brothers = brother.objects.all()
        context = RequestContext(request,{"brothers":brothers, "section":"Active Brothers"})
        return render_to_response('chapter_roll.html',context)
