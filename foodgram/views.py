from django.shortcuts import render
from django.views.generic.base import TemplateView


def page_not_found(request, exception):
    return render(request, "misc/404.html", status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)


class AboutPage(TemplateView):
    template_name = 'flatpages/about.html'


class SpecPage(TemplateView):
    template_name = 'flatpages/technologies.html'
