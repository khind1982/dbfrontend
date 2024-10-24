# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlternativeTitle(models.Model):
    alt_title_id = models.AutoField(primary_key=True)
    alt_title = models.CharField(max_length=5000)
    pqid = models.ForeignKey('EebRecord', models.DO_NOTHING, db_column='pqid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alternative_title'


class Classifications(models.Model):
    class_id = models.AutoField(primary_key=True)
    classification = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'classifications'


class Collections(models.Model):
    collection_id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'collections'


class CommentCodes(models.Model):
    comment_code_id = models.AutoField(primary_key=True)
    comment_code = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'comment_codes'


class CopCerl(models.Model):
    name = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    type_sort = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cop_cerl'


class CountriesOfPublication(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_of_publication = models.CharField(max_length=255)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries_of_publication'


class CountryCodes(models.Model):
    code = models.CharField(max_length=5)
    country = models.CharField(max_length=44)

    class Meta:
        managed = False
        db_table = 'country_codes'


class EebAuthor(models.Model):
    aut_id = models.AutoField(primary_key=True)
    author_corrected = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_uninverted = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    date_of_death = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    person_title = models.CharField(max_length=255, blank=True, null=True)
    professional_title = models.CharField(max_length=255, blank=True, null=True)
    corporate_author = models.CharField(max_length=255, blank=True, null=True)
    author_isni = models.CharField(max_length=50, blank=True, null=True)
    author_viaf = models.CharField(max_length=100, blank=True, null=True)
    lionid = models.CharField(max_length=255, blank=True, null=True)
    do_not_normalize = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eeb_author'


class EebCorporateNames(models.Model):
    name = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    type_sort = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eeb_corporate_names'


class EebPersonalNames(models.Model):
    name = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    type_sort = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eeb_personal_names'


class EebRecord(models.Model):
    pqid = models.CharField(primary_key=True, max_length=255)
    unit = models.CharField(max_length=20)
    source_library = models.CharField(max_length=100)
    title = models.CharField(max_length=5000)
    displaydate = models.CharField(max_length=50)
    startdate = models.CharField(max_length=8)
    enddate = models.CharField(max_length=8, blank=True, null=True)
    imprint = models.CharField(max_length=500, blank=True, null=True)
    ustc_bibliographic_reference = models.CharField(max_length=50, blank=True, null=True)
    shelfmark = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    pagination = models.CharField(max_length=255, blank=True, null=True)
    source_collection = models.CharField(max_length=255, blank=True, null=True)
    ustc_number = models.CharField(max_length=50, blank=True, null=True)
    ustc_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eeb_record'


class Illustrations(models.Model):
    illus_id = models.AutoField(primary_key=True)
    illustration = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'illustrations'


class ImpCerl(models.Model):
    name = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    type_sort = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imp_cerl'


class Imprints(models.Model):
    imp_id = models.AutoField(primary_key=True)
    publisher_printer = models.CharField(max_length=255)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprints'


class Itemimages(models.Model):
    image_id = models.AutoField(primary_key=True)
    itemimagefile1 = models.CharField(max_length=34)
    colour = models.CharField(max_length=10)
    imagenumber = models.CharField(max_length=1000)
    ordernum = models.CharField(max_length=1000)
    orderlabel = models.CharField(max_length=50, blank=True, null=True)
    pagecontent = models.CharField(max_length=100, blank=True, null=True)
    pagetype = models.CharField(max_length=50, blank=True, null=True)
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemimages'


class LanguageCodes(models.Model):
    code = models.CharField(max_length=5)
    language = models.CharField(max_length=55)

    class Meta:
        managed = False
        db_table = 'language_codes'


class Languages(models.Model):
    lang_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Libraries(models.Model):
    library_id = models.AutoField(primary_key=True)
    source_library = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'libraries'


class Links(models.Model):
    link_id = models.CharField(primary_key=True, max_length=50)
    linktitle = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'links'


class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_name = models.CharField(max_length=5000, blank=True, null=True)
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    note_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notes'


class PlacesOfPublication(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_of_publication = models.CharField(max_length=255)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places_of_publication'


class PopCerl(models.Model):
    name = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    type_sort = models.CharField(max_length=1, blank=True, null=True)
    cerlid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pop_cerl'


class RecordToAuthor(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid')
    aut = models.ForeignKey(EebAuthor, models.DO_NOTHING)
    main_author = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'record_to_author'


class RecordToClassification(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    class_field = models.ForeignKey(Classifications, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'record_to_classification'


class RecordToCommentCode(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    comment_code = models.ForeignKey(CommentCodes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_comment_code'


class RecordToCountries(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    country = models.ForeignKey(CountriesOfPublication, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_countries'


class RecordToIllustration(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    illus = models.ForeignKey(Illustrations, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_illustration'


class RecordToImprints(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    imp = models.ForeignKey(Imprints, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_imprints'


class RecordToLanguage(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    lang = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_language'


class RecordToLinks(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    link = models.ForeignKey(Links, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_links'


class RecordToPlaces(models.Model):
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)
    place = models.ForeignKey(PlacesOfPublication, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_to_places'


class Sizes(models.Model):
    size_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=500)
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sizes'


class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class TestTable(models.Model):
    docid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_table'


class Volumeimages(models.Model):
    image_id = models.AutoField(primary_key=True)
    volumeimagefile = models.CharField(max_length=34)
    colour = models.CharField(max_length=10)
    imagenumber = models.CharField(max_length=1000)
    ordernum = models.CharField(max_length=1000)
    orderlabel = models.CharField(max_length=50, blank=True, null=True)
    pagecontent = models.CharField(max_length=100, blank=True, null=True)
    pagetype = models.CharField(max_length=50, blank=True, null=True)
    pqid = models.ForeignKey(EebRecord, models.DO_NOTHING, db_column='pqid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volumeimages'
