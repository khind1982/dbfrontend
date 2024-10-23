from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def show_eeb_record_table(request):
    template = loader.get_template("eeb_record.html")
    return HttpResponse(template.render())
    # return HttpResponse("Hello world!")
