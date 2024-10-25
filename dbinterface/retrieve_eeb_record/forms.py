from django import forms

from .models import EebRecord

from retrieve_eeb_record import models

# from retrieve_eeb_record.forms import ShelfmarkForm


class EEBRecordForm(forms.ModelForm):
    entry = forms.CharField()

    class Meta:
        model = models.Settings
        fields = ["entry"]


# class EEBRecordForm(forms.ModelForm):
#     class Meta:
#         model = EebRecord
#         fields = "__all__"
