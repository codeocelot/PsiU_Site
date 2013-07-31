# Create your views here.

from forms import email_form
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail

def email(request):
  if request.method == 'POST':
    form = email_form(request.POST)
    if form.is_valid():
      to_addr = form.cleaned_data['to_addr']
      from_addr = form.cleaned_data['from_addr']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']
      send_mail(subject,message,from_addr,to_addr)
      return HttpResponseRedirect('/thanks/')
  else:
    form = email_form()
  return render(request,'email_form.html', {
    'email_form': form,
    })