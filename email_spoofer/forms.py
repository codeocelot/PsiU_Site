from django import forms

class email_form(forms.Form):
  to_addr = forms.CharField(max_length=100)
  from_addr = forms.CharField(max_length=100)
  subject = forms.CharField(max_length=100)
  message = forms.CharField(max_length=10000)
