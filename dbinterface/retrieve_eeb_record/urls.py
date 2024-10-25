from django.urls import path
from . import views

# In the following example, 'show_eeb_record_table'
# is the name of the view function in views.py

urlpatterns = [
    path("eeb_record_display", views.EEBRecordData.as_view(), name="home"),
]
