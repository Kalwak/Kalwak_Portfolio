from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import EmailForm


@api_view(['POST'])
def SendEmail(request):
    '''
    Post Method that sends a Email from the 'Contact us' page form
    to the group Email.
    '''
    Email = request.data.get("Email", None)
    Subject = request.data.get("Subject", None)
    Body = request.data.get("Body", None)
    Email = EmailMessage(Subject, '%s \n From %s' % (Body, Email),
                         to=['winkemail@gmail.com', ])
    Response = Email.send()
    Response = {"response": Response}
    return JsonResponse(Response)


class EmailListView(ListView):
    template_name = "ejemplo.html"
    queryset = ""  # EmailForm.objects.all() #comando para colectar todos los objetos (en este caso no tiene)
