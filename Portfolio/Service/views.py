import json
import os

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from ipware import get_client_ip
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rivescript import RiveScript

from Portfolio import settings
from Portfolio.settings import BASE_DIR
from Service.serializers import ChatbotSerializer, FileSerializer, ServiceSerializer
from .models import ServiceRequest
from rest_framework import viewsets
from .serializers import ServiceRequestSerializer
from rest_framework import status
from rest_framework.response import Response
import logging

log = logging.getLogger('debugger')


def save_files(files, pk):
    data = [

    ]
    if len(files) and files[
        0] != '':  # Must be done, since posting a form with no files defaults the file's value to ''
        for element in files:
            data.append({
                "service": pk,
                "file": element
            })
    if len(data):
        files = FileSerializer(data=data, many=True)
        if files.is_valid():
            files.save()
        else:
            return Response(files.errors, status=status.HTTP_400_BAD_REQUEST)


def save_services(services, pk):
    data = [

    ]
    for element in services:
        data.append({
            "service_request": pk,
            "service": element
        })
    if len(data):
        services = ServiceSerializer(data=data, many=True)
        if services.is_valid():
            services.save()
        else:
            return Response(services.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRequestView(viewsets.ModelViewSet):
    serializer_class = ServiceRequestSerializer
    queryset = ServiceRequest.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Api view that saves a ServiceRequest and internally sends an email
        to website owners. To see this implementation go to:
        :func:`Service.serializers.ServiceRequestSerializer.create`

        :params request: should contain a JSON with name, email, description.
                        Also, can have attached several files.
        """
        mutable = request.POST._mutable

        request.POST._mutable = True
        files = request.data.pop("files", [])
        services = request.data.pop("services", [])

        request.POST._mutable = mutable
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid():
            log.info('Request data is valid.')
            instance = serializer.save()

            error = save_files(files, instance.pk)
            if error:
                return error
            error = save_services(services, instance.pk)
            if error:
                return error

            return redirect(f"{settings.FRONTEND_URL}/hire-us/", status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        log.info('Request data is not valid.')
        errors_json = JSONRenderer().render(serializer.errors)
        errors_json = json.loads(errors_json)
        return redirect(f"{settings.FRONTEND_URL}/hire-us/?errors={errors_json}", status=status.HTTP_400_BAD_REQUEST)


class ChatbotAPIView(APIView):
    """
    An API that only accepts post data and sends it to the rivescript kalwak bot to be processed. It is meant to
    be displayed in the kalwak frontend as a chatbot.
    """
    serializer_class = ChatbotSerializer
    rs = RiveScript()

    def __init__(self):
        """
        Upon the creation of this class we must load the rivescript chatbot scripts and save it to an attribute. This
        has to be done in the init otherwise user data will not be saved to the bot, such as the user's name.
        """
        super(ChatbotAPIView, self).__init__()
        try:
            self.rs.load_directory(os.path.join(BASE_DIR, "chatbot_scripts"))
            self.rs.sort_replies()
            log.debug("Rivescript scripts and instances loaded.")
        except Exception as e:
            log.error(str(e))

    def post(self, request):
        """
        This api view is used to get input from the user and transform it accordingly using rivescript and return it.
        It must receive json data as follows:

        msg: the message you want to send to the rivescript kalwak bot,
        ip: an identifier for the kalwak bot to use

        :return: The kalwak bot response or the serializer errors
        """

        if not request.data:  # No data was sent, so send a default response
            desc = self.rs.get_variable(name="desc")
            return Response(desc)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            msg = request.POST.get('msg') or request.data.get('msg')
            ip = request.POST.get('ip') or request.data.get('ip')
            anchor_href = request.data.get('current_vue_path') + "#contact-section"
            self.rs.set_variable(name="anchor_contact_us_url", value=anchor_href)
            reply = self.rs.reply(ip, msg)
            log.info('Request data is valid.')
            return Response(reply)
        log.info('Request data is not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetIP(APIView):
    """
    Return the ip of the client to be used with the rivescript chatbot, exclusively as a GET request
    """

    def get(self, request):
        ip = get_client_ip(request)[0]
        response = {
            "ip": ip
        }
        return JsonResponse(response)
