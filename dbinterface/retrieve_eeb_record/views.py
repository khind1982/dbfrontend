from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.list import ListView
from django.urls import reverse

from .forms import EEBRecordForm

from .models import EebRecord

from multi_form_view import MultiModelFormView


class EEBRecordData(MultiModelFormView):

    form_classes = {"eeb_record_form": EEBRecordForm}
    template_name = "eeb_record.html"
    eebrecord = EebRecord.objects.all().values()

    def get_success_url(self):
        return reverse("home")

    def forms_valid(self, forms):
        eeb_record = forms["eeb_record_form"].save(commit=False)
        return super(EEBRecordData, self).forms_valid(forms)

    def get(self, request, *args, **kwargs):
        context = {}
        context["record"] = EebRecord.objects.all().values()
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        context = {}
        user_response = [
            (identifier, value) for identifier, value in request.POST.items()
        ][1]
        pqid, columnidentifier = user_response[0].split("|")
        value = user_response[-1]
        identifier_to_column = {"shelf": "shelfmark", "ddate": "displaydate"}
        record = EebRecord.objects.filter(pqid=pqid)[0]
        setattr(record, identifier_to_column[columnidentifier], value)
        record.save()

        context["record"] = EebRecord.objects.all().values()
        return self.render_to_response(context)


def fruits(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))
