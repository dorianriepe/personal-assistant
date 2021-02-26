from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))