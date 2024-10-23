from django.urls import path
from . import views

# In the following example, 'show_eeb_record_table'
# is the name of the view function in views.py

urlpatterns = [
    path(
        "show_eeb_record_table/",
        views.show_eeb_record_table,
        name="show_eeb_record_table",
    )
]
