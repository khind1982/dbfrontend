from django.test import TestCase

from .views import EEBRecordData


# Create your tests here.
class EEBRecordViewTests(TestCase):
    def test_update_record_with_responses_record_title(self):
        record = EEBRecordData()
        test_response = ("fra-bnf-ars-00002967-002|shelf", "new")
        actual = record.update_record_with_responses(test_response)
        self.assertEquals(actual, "")
