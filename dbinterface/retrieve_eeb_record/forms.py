from django import forms

from .models import EebRecord

from retrieve_eeb_record import models


class EEBRecordForm(forms.ModelForm):
    entry = forms.CharField()

    class Meta:
        model = models.Settings
        fields = ["entry"]
