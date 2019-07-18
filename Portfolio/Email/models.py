from django.db import models
from django import forms


class EmailForm(forms.Form):
    Subject = forms.CharField(label='Subject', max_length=100)
    Message = forms.CharField(label='Message', max_length=1000)
    Client_email = forms.EmailField(label='Email')
