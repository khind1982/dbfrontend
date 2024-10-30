import sys
import os
import pytest

from io import StringIO

from django.http import request
from django.http import QueryDict
from django.core.handlers.wsgi import WSGIRequest

import lxml.etree as et

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from retrieve_eeb_record import views, models


def test_views_fruits_template():
    actual = views.fruits(request)
    xmlactual = et.fromstring(actual.content)
    print(xmlactual.xpath(".//h1")[0].text)
    assert xmlactual.xpath(".//h1")[0].text == "Apple"


def test_model_eebrecord():
    actual = models.EebRecord
    assert getattr(actual, "title")
    with pytest.raises(AttributeError):
        assert getattr(actual, "shelfmark_number")


def test_views_response_object():
    response = WSGIRequest({"REQUEST_METHOD": "POST", "wsgi.input": StringIO})
    response.POST = QueryDict("", mutable=True)
    response.POST["csrfmiddlewaretoken"] = "test"
    response.POST["example1|ddate"] = ["1648"]
    actual = views.parse_response(response)
    assert actual == ("example1", "ddate", ["1648"])
