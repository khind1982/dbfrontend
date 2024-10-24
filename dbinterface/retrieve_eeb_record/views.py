from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import EebRecord


def show_eeb_record_table(request):
    mymembers = EebRecord.objects.all().values()
    template = loader.get_template("eeb_record.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello world!")
