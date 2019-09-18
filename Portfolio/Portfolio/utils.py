import json
from json import JSONDecodeError

import django
from django.http import RawPostDataException
from ipware import get_client_ip

from Project.models import Logs

"""
These utilities are made to helpout with the UserLogMiddleware
"""


def get_response(response):
    """
    Used to get content of a response if it has and it can be parsed into json
    :return: Json form of the content of the response
    """
    try:
        out = response.content
        out = json.loads(out)
    except (AttributeError, JSONDecodeError):
        out = "No json response"
    return out


def get_request(request):
    """
    Used to get body of a request if it has and it can be parsed into json
    :return: Json form of the content of the request
    """
    try:
        out = request.body
        out = json.loads(out)
    except (AttributeError, JSONDecodeError):
        out = "No json request"
    except UnicodeDecodeError:  # This happens when a file is sent
        out = str(request.FILES)
    except RawPostDataException:
        out = "Error on accessing the request data"
    return out


def get_status_text(request):
    """
    Used to get the status text of a request if it has it and it can be parsed into json
    :return: Status text of request
    """
    try:
        out = request.status_text
    except AttributeError:
        out = "No status text."
    return out


def contains_unwanted_path(path: str):
    """
    Checks if an unwanted path is in the path provided as an argument.
    :param path: A path in an url
    :return: A boolean saying if one of the unwanted paths are in the path
    """
    unwanted_paths = [
        "/admin",
        "/robots.txt",
        "/favicon.ico",
        "/assets/",
        "/static/",
    ]

    for unwanted_path in unwanted_paths:
        if path.startswith(unwanted_path):
            return True
    return False


def create_log(response, request):
    """
    Creates a new log entry with all the fields needed using the request and the response
    but only if it not a request to the admin page.
    :return: The object created
    """
    _path = request.get_full_path()
    if contains_unwanted_path(_path):
        return
    _status_code = response.status_code
    _status_text = get_status_text(request)
    _response = get_response(response)
    _request = get_request(request)
    _is_ajax = request.is_ajax()
    _is_secure = request.is_secure()
    _ipv4_address = get_client_ip(request)[0]
    log = Logs.objects.create(status_code=_status_code, status_text=_status_text, response=_response,
                              request=_request, path=_path, is_ajax=_is_ajax, is_secure=_is_secure,
                              ipv4_address=_ipv4_address)
    return log
