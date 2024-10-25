from django.db import models


# Create your models here.
class EebRecord(models.Model):
    pqid = models.CharField(primary_key=True, max_length=255)
    unit = models.CharField(max_length=20)
    source_library = models.CharField(max_length=100)
    title = models.CharField(max_length=5000)
    displaydate = models.CharField(max_length=50)
    startdate = models.CharField(max_length=8)
    enddate = models.CharField(max_length=8, blank=True, null=True)
    imprint = models.CharField(max_length=500, blank=True, null=True)
    ustc_bibliographic_reference = models.CharField(
        max_length=50, blank=True, null=True
    )
    shelfmark = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    pagination = models.CharField(max_length=255, blank=True, null=True)
    source_collection = models.CharField(max_length=255, blank=True, null=True)
    ustc_number = models.CharField(max_length=50, blank=True, null=True)
    ustc_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "eeb_record"


class Settings(models.Model):
    shelfmark = models.TextField()
