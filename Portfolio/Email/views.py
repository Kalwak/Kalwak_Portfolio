from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.http import JsonResponse

#class SendEmailSerializer(Serializer.Serializer):
    #Email = serializers.Charfield()

#class SendEmailView(viewset.ModelViewset):
    
    #def post(request):
        #serialized_data = SendEmail(request.POST)
        #if serialized_data.is_valid():
            #return Response({"detail":"enviado"})
        #return Response(serialized_data.errors)
# Ejemplo de viewset para hacer CRUD
#class SendEmailView(viewset.ModelViewset):
    #model = Correos

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
