import sys
import os

from django.http import request

import lxml.etree as et

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from retrieve_eeb_record import views


def test_views_fruits_template():
    actual = views.fruits(request)
    xmlactual = et.fromstring(actual.content)
    print(xmlactual.xpath(".//h1")[0].text)
    assert xmlactual.xpath(".//h1")[0].text == "Apple"
