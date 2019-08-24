from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class VuejsFrontend(TemplateView):
    template_name = "index.html"


def vuejs_frontend404(request, exception):
    return render_to_response("index.html", context={})
