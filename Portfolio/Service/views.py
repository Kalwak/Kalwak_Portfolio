import os
from rest_framework.views import APIView
from rivescript import RiveScript
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
    for element in files:
        element["service"] = pk
    files = FileSerializer(data=files, many=True)
    if files.is_valid():
        files.save()
    else:
        return Response(files.errors, status=status.HTTP_400_BAD_REQUEST)


def save_services(services, pk):
    for element in services:
        element["service_request"] = pk
    services = ServiceSerializer(data=services, many=True)
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
        files = request.data.pop("files", [])
        services = request.data.pop("services", [])
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

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        log.info('Request data is not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            msg = request.POST.get('msg') or request.data.get('msg')
            ip = request.POST.get('ip') or request.data.get('ip')
            reply = self.rs.reply(ip, msg)
            log.info('Request data is valid.')
            return Response(reply)
        log.info('Request data is not valid.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
