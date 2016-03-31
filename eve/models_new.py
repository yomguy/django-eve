# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Accounting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    manifestation_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting'


class AccountingVersion(models.Model):
    id = models.ForeignKey(Accounting, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    manifestation_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'accounting_version'
        unique_together = (('id', 'version'),)


class Addressable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_accessor = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addressable'


class AddressableIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Addressable, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'addressable_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class AddressableVersion(models.Model):
    id = models.ForeignKey(Addressable, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(max_length=255, blank=True, null=True)
    last_accessor_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'addressable_version'
        unique_together = (('id', 'version'),)


class Attachment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey('Email', models.DO_NOTHING)
    original_name = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    mime_type = models.TextField(blank=True, null=True)
    size = models.FloatField()
    version = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attachment'


class AttachmentVersion(models.Model):
    id = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='id')
    email_id = models.BigIntegerField()
    original_name = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    mime_type = models.TextField(blank=True, null=True)
    size = models.FloatField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'attachment_version'
        unique_together = (('id', 'version'),)


class Authentication(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    success = models.NullBooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authentication'


class AutoGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_group'


class BankPayment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    payment_id = models.BigIntegerField(blank=True, null=True)
    serialized = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    merchant_country = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_means = models.TextField(blank=True, null=True)
    transmission_date = models.CharField(max_length=255, blank=True, null=True)
    payment_time = models.CharField(max_length=255, blank=True, null=True)
    payment_certificate = models.CharField(max_length=255, blank=True, null=True)
    authorization_id = models.CharField(max_length=255, blank=True, null=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    cvv_flag = models.CharField(max_length=255, blank=True, null=True)
    bank_response_code = models.CharField(max_length=255, blank=True, null=True)
    complementary_code = models.CharField(max_length=255, blank=True, null=True)
    complementary_info = models.CharField(max_length=255, blank=True, null=True)
    return_context = models.CharField(max_length=255, blank=True, null=True)
    caddie = models.TextField(blank=True, null=True)
    receipt_complement = models.TextField(blank=True, null=True)
    merchant_language = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_ip_address = models.CharField(max_length=255, blank=True, null=True)
    capture_day = models.CharField(max_length=255, blank=True, null=True)
    capture_mode = models.CharField(max_length=255, blank=True, null=True)
    data_field = models.CharField(max_length=255, blank=True, null=True)
    cvv_response_code = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.CharField(max_length=255, blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank_payment'


class BoughtProduct(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    product_declination = models.ForeignKey('ProductDeclination', models.DO_NOTHING, blank=True, null=True)
    price = models.ForeignKey('Price', models.DO_NOTHING, blank=True, null=True)
    vat_0 = models.ForeignKey('Vat', models.DO_NOTHING, db_column='vat_id', blank=True, null=True)  # Field renamed because of name conflict.
    name = models.CharField(max_length=255)
    declination = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    price_name = models.CharField(max_length=255)
    integrated_at = models.DateTimeField(blank=True, null=True)
    description_for_buyers = models.TextField(blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    member_card = models.ForeignKey('MemberCard', models.DO_NOTHING, blank=True, null=True)
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING, blank=True, null=True)
    shipping_fees = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_fees_vat = models.DecimalField(max_digits=5, decimal_places=4)
    destocked = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bought_product'


class BoughtProductVersion(models.Model):
    id = models.ForeignKey(BoughtProduct, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    product_declination_id = models.BigIntegerField(blank=True, null=True)
    price_id = models.BigIntegerField(blank=True, null=True)
    vat_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    declination = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    price_name = models.CharField(max_length=255)
    integrated_at = models.DateTimeField(blank=True, null=True)
    description_for_buyers = models.TextField(blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    member_card_id = models.BigIntegerField(blank=True, null=True)
    ticket_id = models.BigIntegerField(blank=True, null=True)
    shipping_fees = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_fees_vat = models.DecimalField(max_digits=5, decimal_places=4)
    destocked = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bought_product_version'
        unique_together = (('id', 'version'),)


class Cache(models.Model):
    id = models.BigIntegerField(primary_key=True)
    content = models.BinaryField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cache'


class CacheVersion(models.Model):
    id = models.ForeignKey(Cache, models.DO_NOTHING, db_column='id')
    content = models.BinaryField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_version'
        unique_together = (('id', 'version'),)


class Cancellation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancellation'


class CancellationVersion(models.Model):
    id = models.ForeignKey(Cancellation, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    ticket_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cancellation_version'
        unique_together = (('id', 'version'),)


class Checkpoint(models.Model):
    id = models.BigIntegerField(primary_key=True)
    event = models.ForeignKey('Event', models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    organism = models.ForeignKey('Organism', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkpoint'


class Color(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'color'


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_accessor = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    firstname = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    flash_on_control = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    family_contact = models.BooleanField()
    organism_category = models.ForeignKey('OrganismCategory', models.DO_NOTHING, blank=True, null=True)
    confirmed = models.BooleanField()
    familial_quotient = models.ForeignKey('FamilialQuotient', models.DO_NOTHING, blank=True, null=True)
    type_of_resources = models.ForeignKey('TypeOfResources', models.DO_NOTHING, blank=True, null=True)
    familial_situation = models.ForeignKey('FamilialSituation', models.DO_NOTHING, blank=True, null=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    culture = models.CharField(max_length=32, blank=True, null=True)
    picture = models.ForeignKey('Picture', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactArchive(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    old_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contact_archive'


class ContactEntry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    professional = models.ForeignKey('Professional', models.DO_NOTHING)
    comment1 = models.TextField(blank=True, null=True)
    comment2 = models.TextField(blank=True, null=True)
    confirmed = models.NullBooleanField()
    entry = models.ForeignKey('Entry', models.DO_NOTHING)
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_entry'


class ContactEventArchives(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    happens_at = models.DateTimeField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_event_archives'


class ContactIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Contact, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'contact_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class ContactPhonenumber(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_phonenumber'


class ContactRelationship(models.Model):
    id = models.BigIntegerField(primary_key=True)
    from_contact = models.ForeignKey(Contact, models.DO_NOTHING)
    to_contact = models.ForeignKey(Contact, models.DO_NOTHING)
    contact_relationship_type = models.ForeignKey('ContactRelationshipType', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_relationship'


class ContactRelationshipType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_relationship_type'


class ContactVersion(models.Model):
    id = models.ForeignKey(Contact, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(max_length=255, blank=True, null=True)
    last_accessor_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    firstname = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    flash_on_control = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    family_contact = models.BooleanField()
    organism_category_id = models.BigIntegerField(blank=True, null=True)
    confirmed = models.BooleanField()
    familial_quotient_id = models.BigIntegerField(blank=True, null=True)
    type_of_resources_id = models.BigIntegerField(blank=True, null=True)
    familial_situation_id = models.BigIntegerField(blank=True, null=True)
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    culture = models.CharField(max_length=32, blank=True, null=True)
    picture_id = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contact_version'
        unique_together = (('id', 'version'),)


class Control(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)
    checkpoint = models.ForeignKey(Checkpoint, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control'


class ControlVersion(models.Model):
    id = models.ForeignKey(Control, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    ticket_id = models.BigIntegerField()
    checkpoint_id = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'control_version'
        unique_together = (('id', 'version'),)


class Domain(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'domain'


class Email(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    field_from = models.CharField(max_length=255)
    field_to = models.TextField(blank=True, null=True)
    field_cc = models.TextField(blank=True, null=True)
    field_bcc = models.TextField(blank=True, null=True)
    field_subject = models.TextField()
    content = models.TextField()
    content_text = models.TextField(blank=True, null=True)
    sent = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class EmailAction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    type = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    professional = models.ForeignKey('Professional', models.DO_NOTHING, blank=True, null=True)
    organism = models.ForeignKey('Organism', models.DO_NOTHING, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_action'


class EmailContact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_contact'


class EmailExternalLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    original_url = models.CharField(max_length=255)
    encrypted_uri = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_external_link'


class EmailIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Email, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'email_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class EmailLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_link'


class EmailOrganism(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    organism = models.ForeignKey('Organism', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_organism'


class EmailProfessional(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    professional = models.ForeignKey('Professional', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_professional'


class EmailSpool(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    priority = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_spool'


class EmailTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template'


class Entry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    event = models.ForeignKey('Event', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'entry'


class EntryElement(models.Model):
    id = models.BigIntegerField(primary_key=True)
    manifestation_entry = models.ForeignKey('ManifestationEntry', models.DO_NOTHING)
    contact_entry = models.ForeignKey(ContactEntry, models.DO_NOTHING)
    second_choice = models.BooleanField()
    accepted = models.BooleanField()
    impossible = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'entry_element'


class EntryTickets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    entry_element = models.ForeignKey(EntryElement, models.DO_NOTHING)
    price = models.ForeignKey('Price', models.DO_NOTHING)
    quantity = models.BigIntegerField()
    gauge = models.ForeignKey('Gauge', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'entry_tickets'
        unique_together = (('entry_element', 'price'),)


class Event(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    meta_event = models.ForeignKey('MetaEvent', models.DO_NOTHING)
    event_category = models.ForeignKey('EventCategory', models.DO_NOTHING, blank=True, null=True)
    event_category_description = models.CharField(max_length=255, blank=True, null=True)
    staging = models.CharField(max_length=255, blank=True, null=True)
    staging_label = models.CharField(max_length=255, blank=True, null=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    writer_label = models.CharField(max_length=255, blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    age_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    age_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    web_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    web_price_group = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ForeignKey('Picture', models.DO_NOTHING, blank=True, null=True)
    display_by_default = models.BooleanField()
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    museum = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    vat = models.ForeignKey('Vat', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_category'


class EventCompany(models.Model):
    organism = models.ForeignKey('Organism', models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_company'
        unique_together = (('organism', 'event'),)


class EventIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Event, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'event_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class EventTranslation(models.Model):
    id = models.ForeignKey(Event, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=127, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    extradesc = models.TextField(blank=True, null=True)
    extraspec = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'event_translation'
        unique_together = (('id', 'lang'),)


class EventVersion(models.Model):
    id = models.ForeignKey(Event, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=127, blank=True, null=True)
    meta_event_id = models.BigIntegerField()
    event_category_id = models.BigIntegerField(blank=True, null=True)
    event_category_description = models.CharField(max_length=255, blank=True, null=True)
    staging = models.CharField(max_length=255, blank=True, null=True)
    staging_label = models.CharField(max_length=255, blank=True, null=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    writer_label = models.CharField(max_length=255, blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    age_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    age_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    extradesc = models.TextField(blank=True, null=True)
    extraspec = models.TextField(blank=True, null=True)
    web_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    web_price_group = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    picture_id = models.BigIntegerField(blank=True, null=True)
    display_by_default = models.BooleanField()
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    museum = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'event_version'
        unique_together = (('id', 'version', 'lang'),)


class FailedControl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    ticket_id = models.CharField(max_length=255, blank=True, null=True)
    checkpoint_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'failed_control'


class FailedControlVersion(models.Model):
    id = models.ForeignKey(FailedControl, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    ticket_id = models.CharField(max_length=255, blank=True, null=True)
    checkpoint_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'failed_control_version'
        unique_together = (('id', 'version'),)


class FamilialQuotient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familial_quotient'


class FamilialSituation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familial_situation'


class Filter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    filter = models.TextField()

    class Meta:
        managed = False
        db_table = 'filter'
        unique_together = (('name', 'type', 'sf_guard_user'),)


class Gauge(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workspace = models.ForeignKey('Workspace', models.DO_NOTHING)
    manifestation = models.ForeignKey('Manifestation', models.DO_NOTHING)
    value = models.BigIntegerField()
    online = models.BooleanField()
    onsite = models.BooleanField()
    group_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gauge'
        unique_together = (('manifestation', 'workspace'),)


class GeoFrDepartment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geo_fr_region = models.ForeignKey('GeoFrRegion', models.DO_NOTHING)
    num = models.CharField(unique=True, max_length=3)
    name = models.CharField(max_length=255)
    strict_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_fr_department'


class GeoFrRegion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    strict_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_fr_region'


class GroupAutoUser(models.Model):
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)
    information = models.TextField(blank=True, null=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_auto_user'
        unique_together = (('group', 'sf_guard_user'),)


class GroupContact(models.Model):
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)
    information = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_contact'
        unique_together = (('group', 'contact'),)


class GroupDeleted(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_deleted'


class GroupDetail(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_detail'


class GroupOrganism(models.Model):
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)
    information = models.TextField(blank=True, null=True)
    organism = models.ForeignKey('Organism', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_organism'
        unique_together = (('group', 'organism'),)


class GroupProfessional(models.Model):
    group = models.ForeignKey('GroupTable', models.DO_NOTHING)
    information = models.TextField(blank=True, null=True)
    professional = models.ForeignKey('Professional', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_professional'
        unique_together = (('group', 'professional'),)


class GroupTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    picture = models.ForeignKey('Picture', models.DO_NOTHING, blank=True, null=True)
    display_everywhere = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_table'


class GroupUser(models.Model):
    group = models.ForeignKey(GroupTable, models.DO_NOTHING)
    information = models.TextField(blank=True, null=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_user'
        unique_together = (('group', 'sf_guard_user'),)


class GroupWorkspace(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workspace = models.ForeignKey('Workspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_workspace'


class Hold(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    public_name = models.CharField(max_length=255, blank=True, null=True)
    manifestation = models.ForeignKey('Manifestation', models.DO_NOTHING)
    next = models.ForeignKey('self', models.DO_NOTHING, db_column='next', blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    price = models.ForeignKey('Price', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hold'


class HoldContent(models.Model):
    seat = models.ForeignKey('Seat', models.DO_NOTHING)
    hold = models.ForeignKey(Hold, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hold_content'
        unique_together = (('seat', 'hold'),)


class HoldTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    hold = models.ForeignKey(Hold, models.DO_NOTHING)
    rank = models.FloatField()
    pretickets = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hold_transaction'


class HoldTransactionVersion(models.Model):
    id = models.ForeignKey(HoldTransaction, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    hold_id = models.BigIntegerField()
    rank = models.FloatField()
    pretickets = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'hold_transaction_version'
        unique_together = (('id', 'version'),)


class HoldTranslation(models.Model):
    id = models.ForeignKey(Hold, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'hold_translation'
        unique_together = (('id', 'lang'),)


class HoldVersion(models.Model):
    id = models.ForeignKey(Hold, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    public_name = models.CharField(max_length=255, blank=True, null=True)
    manifestation_id = models.BigIntegerField()
    next = models.BigIntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    price_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'hold_version'
        unique_together = (('id', 'version', 'lang'),)


class Invoice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    type = models.CharField(max_length=255, blank=True, null=True)
    manifestation = models.ForeignKey('Manifestation', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceVersion(models.Model):
    id = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    manifestation_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_version'
        unique_together = (('id', 'version'),)


class Itemable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemable'


class ItemableVersion(models.Model):
    id = models.ForeignKey(Itemable, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'itemable_version'
        unique_together = (('id', 'version'),)


class Jabber(models.Model):
    id = models.BigIntegerField(primary_key=True)
    jabber_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'jabber'


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_accessor = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    rank = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    organism = models.ForeignKey('Organism', models.DO_NOTHING, blank=True, null=True)
    gauge_max = models.BigIntegerField(blank=True, null=True)
    gauge_min = models.BigIntegerField(blank=True, null=True)
    reservation_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    place = models.BooleanField()
    licenses = models.CharField(max_length=255, blank=True, null=True)
    unlimited = models.NullBooleanField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class LocationBooking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    manifestation = models.ForeignKey('Manifestation', models.DO_NOTHING)
    location = models.ForeignKey(Location, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'location_booking'


class LocationIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Location, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'location_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class LocationVersion(models.Model):
    id = models.ForeignKey(Location, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(max_length=255, blank=True, null=True)
    last_accessor_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    rank = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_id = models.BigIntegerField(blank=True, null=True)
    organism_id = models.BigIntegerField(blank=True, null=True)
    gauge_max = models.BigIntegerField(blank=True, null=True)
    gauge_min = models.BigIntegerField(blank=True, null=True)
    reservation_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    place = models.BooleanField()
    licenses = models.CharField(max_length=255, blank=True, null=True)
    unlimited = models.NullBooleanField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'location_version'
        unique_together = (('id', 'version'),)


class Manifestation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    color = models.ForeignKey(Color, models.DO_NOTHING, blank=True, null=True)
    happens_at = models.DateTimeField()
    duration = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vat = models.ForeignKey('Vat', models.DO_NOTHING)
    online_limit = models.BigIntegerField()
    online_limit_per_transaction = models.BigIntegerField(blank=True, null=True)
    no_print = models.BooleanField()
    depends_on = models.ForeignKey('self', models.DO_NOTHING, db_column='depends_on', blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    organism = models.ForeignKey('Organism', models.DO_NOTHING, blank=True, null=True)
    blocking = models.BooleanField()
    reservation_begins_at = models.DateTimeField()
    reservation_ends_at = models.DateTimeField()
    reservation_description = models.TextField(blank=True, null=True)
    reservation_optional = models.BooleanField()
    reservation_confirmed = models.BooleanField()
    expected_income = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    voucherized = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifestation'


class ManifestationContact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contact_id = models.BigIntegerField()
    manifestation_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'manifestation_contact'


class ManifestationEntry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)
    entry = models.ForeignKey(Entry, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manifestation_entry'
        unique_together = (('manifestation', 'entry'),)


class ManifestationExtraInformation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    checked = models.BooleanField()
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifestation_extra_information'


class ManifestationExtraInformationVersion(models.Model):
    id = models.ForeignKey(ManifestationExtraInformation, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    checked = models.BooleanField()
    manifestation_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'manifestation_extra_information_version'
        unique_together = (('id', 'version'),)


class ManifestationOrganizer(models.Model):
    organism = models.ForeignKey('Organism', models.DO_NOTHING)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'manifestation_organizer'
        unique_together = (('organism', 'manifestation'),)


class ManifestationVersion(models.Model):
    id = models.ForeignKey(Manifestation, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    event_id = models.BigIntegerField()
    location_id = models.BigIntegerField()
    color_id = models.BigIntegerField(blank=True, null=True)
    happens_at = models.DateTimeField()
    duration = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vat_id = models.BigIntegerField()
    online_limit = models.BigIntegerField()
    online_limit_per_transaction = models.BigIntegerField(blank=True, null=True)
    no_print = models.BooleanField()
    depends_on = models.BigIntegerField(blank=True, null=True)
    contact_id = models.BigIntegerField(blank=True, null=True)
    organism_id = models.BigIntegerField(blank=True, null=True)
    blocking = models.BooleanField()
    reservation_begins_at = models.DateTimeField()
    reservation_ends_at = models.DateTimeField()
    reservation_description = models.TextField(blank=True, null=True)
    reservation_optional = models.BooleanField()
    reservation_confirmed = models.BooleanField()
    expected_income = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    voucherized = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'manifestation_version'
        unique_together = (('id', 'version'),)


class MemberCard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    expire_at = models.DateTimeField()
    active = models.BooleanField()
    member_card_type = models.ForeignKey('MemberCardType', models.DO_NOTHING)
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING, blank=True, null=True)
    checks_count = models.BigIntegerField()
    detail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_card'


class MemberCardPrice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    member_card = models.ForeignKey(MemberCard, models.DO_NOTHING)
    price = models.ForeignKey('Price', models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_card_price'


class MemberCardPriceModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    member_card_type = models.ForeignKey('MemberCardType', models.DO_NOTHING)
    price = models.ForeignKey('Price', models.DO_NOTHING)
    quantity = models.BigIntegerField()
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    autoadd = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_card_price_model'
        unique_together = (('member_card_type', 'price', 'event'),)


class MemberCardPriceModelVersion(models.Model):
    id = models.ForeignKey(MemberCardPriceModel, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    member_card_type_id = models.BigIntegerField()
    price_id = models.BigIntegerField()
    quantity = models.BigIntegerField()
    event_id = models.BigIntegerField(blank=True, null=True)
    autoadd = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'member_card_price_model_version'
        unique_together = (('id', 'version'),)


class MemberCardPriceVersion(models.Model):
    id = models.ForeignKey(MemberCardPrice, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    member_card_id = models.BigIntegerField()
    price_id = models.BigIntegerField()
    event_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'member_card_price_version'
        unique_together = (('id', 'version'),)


class MemberCardType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    public_details = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    product_declination = models.ForeignKey('ProductDeclination', models.DO_NOTHING, blank=True, null=True)
    price = models.ForeignKey('Price', models.DO_NOTHING, blank=True, null=True)
    nb_tickets_mini = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'member_card_type'


class MemberCardTypePromoCode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    member_card_type = models.ForeignKey(MemberCardType, models.DO_NOTHING, blank=True, null=True)
    begins_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_card_type_promo_code'


class MemberCardTypePromoCodeVersion(models.Model):
    id = models.ForeignKey(MemberCardTypePromoCode, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    member_card_type_id = models.BigIntegerField(blank=True, null=True)
    begins_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'member_card_type_promo_code_version'
        unique_together = (('id', 'version'),)


class MemberCardTypeTranslation(models.Model):
    id = models.ForeignKey(MemberCardType, models.DO_NOTHING, db_column='id')
    description = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'member_card_type_translation'
        unique_together = (('id', 'lang'),)


class MemberCardTypeUser(models.Model):
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    member_card_type = models.ForeignKey(MemberCardType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'member_card_type_user'
        unique_together = (('sf_guard_user', 'member_card_type'),)


class MemberCardVersion(models.Model):
    id = models.ForeignKey(MemberCard, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    contact_id = models.BigIntegerField(blank=True, null=True)
    expire_at = models.DateTimeField()
    active = models.BooleanField()
    member_card_type_id = models.BigIntegerField()
    transaction_id = models.BigIntegerField(blank=True, null=True)
    checks_count = models.BigIntegerField()
    detail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'member_card_version'
        unique_together = (('id', 'version'),)


class MetaEvent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hide_in_month_calendars = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_event'


class MetaEventTranslation(models.Model):
    id = models.ForeignKey(MetaEvent, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'meta_event_translation'
        unique_together = (('id', 'lang'), ('name', 'lang'),)


class MetaEventUser(models.Model):
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    meta_event_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'meta_event_user'
        unique_together = (('sf_guard_user', 'meta_event_id'),)


class ModelType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_type'
        unique_together = (('name', 'type'),)


class OptionTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'option_table'
        unique_together = (('name', 'sf_guard_user', 'value', 'type'), ('name', 'sf_guard_user', 'value', 'type'), ('name', 'sf_guard_user', 'value', 'type'), ('name', 'sf_guard_user', 'value', 'type'),)


class OrderTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    type = models.CharField(max_length=255, blank=True, null=True)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_table'


class OrderVersion(models.Model):
    id = models.ForeignKey(OrderTable, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    manifestation_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'order_version'
        unique_together = (('id', 'version'),)


class Organism(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_accessor = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organism_category = models.ForeignKey('OrganismCategory', models.DO_NOTHING, blank=True, null=True)
    administrative_number = models.CharField(max_length=255, blank=True, null=True)
    professional = models.ForeignKey('Professional', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism'


class OrganismCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_category'


class OrganismIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Organism, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'organism_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class OrganismPhonenumber(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'organism_phonenumber'


class OrganismVersion(models.Model):
    id = models.ForeignKey(Organism, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_no_newsletter = models.BooleanField()
    email_npai = models.BooleanField()
    npai = models.BooleanField()
    vcard_uid = models.CharField(max_length=255, blank=True, null=True)
    last_accessor_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organism_category_id = models.BigIntegerField(blank=True, null=True)
    administrative_number = models.CharField(max_length=255, blank=True, null=True)
    professional_id = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'organism_version'
        unique_together = (('id', 'version'),)


class Payment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    member_card = models.ForeignKey(MemberCard, models.DO_NOTHING, blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentMethod(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    account = models.CharField(max_length=63, blank=True, null=True)
    display = models.BooleanField()
    member_card_linked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentVersion(models.Model):
    id = models.ForeignKey(Payment, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    payment_method_id = models.BigIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=3)
    member_card_id = models.BigIntegerField(blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payment_version'
        unique_together = (('id', 'version'),)


class Phonenumber(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'phonenumber'


class Picture(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    content = models.BinaryField()
    width = models.BigIntegerField(blank=True, null=True)
    height = models.BigIntegerField(blank=True, null=True)
    content_encoding = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picture'


class PictureVersion(models.Model):
    id = models.ForeignKey(Picture, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    content = models.BinaryField()
    width = models.BigIntegerField(blank=True, null=True)
    height = models.BigIntegerField(blank=True, null=True)
    content_encoding = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'picture_version'
        unique_together = (('id', 'version'),)


class Postalcode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    postalcode = models.CharField(max_length=7)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'postalcode'


class Price(models.Model):
    id = models.BigIntegerField(primary_key=True)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    online = models.BooleanField()
    hide = models.BooleanField()
    member_card_linked = models.BooleanField()
    rank = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price'


class PriceGauge(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gauge = models.ForeignKey(Gauge, models.DO_NOTHING)
    price = models.ForeignKey(Price, models.DO_NOTHING)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price_gauge'
        unique_together = (('gauge', 'price'),)


class PriceManifestation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)
    price = models.ForeignKey(Price, models.DO_NOTHING)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price_manifestation'
        unique_together = (('manifestation', 'price'),)


class PricePOS(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price = models.ForeignKey(Price, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price_p_o_s'


class PriceProduct(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    price = models.ForeignKey(Price, models.DO_NOTHING)
    value = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price_product'
        unique_together = (('product', 'price'),)


class PriceTranslation(models.Model):
    id = models.ForeignKey(Price, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'price_translation'
        unique_together = (('id', 'lang'),)


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    meta_event = models.ForeignKey(MetaEvent, models.DO_NOTHING, blank=True, null=True)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    picture = models.ForeignKey(Picture, models.DO_NOTHING, blank=True, null=True)
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    vat = models.ForeignKey('Vat', models.DO_NOTHING, blank=True, null=True)
    shipping_fees = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_fees_vat = models.ForeignKey('Vat', models.DO_NOTHING, blank=True, null=True)
    online = models.BooleanField()
    use_stock = models.BooleanField()
    online_limit = models.BigIntegerField()
    online_limit_per_transaction = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vat = models.ForeignKey('Vat', models.DO_NOTHING, blank=True, null=True)
    online = models.BooleanField()
    product_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductCategoryIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(ProductCategory, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'product_category_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class ProductCategoryTranslation(models.Model):
    id = models.ForeignKey(ProductCategory, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'product_category_translation'
        unique_together = (('id', 'lang'),)


class ProductDeclination(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    prioritary = models.NullBooleanField()
    use_stock = models.BooleanField()
    stock = models.BigIntegerField()
    stock_perfect = models.BigIntegerField()
    stock_critical = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_declination'


class ProductDeclinationIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(ProductDeclination, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'product_declination_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class ProductDeclinationTranslation(models.Model):
    id = models.ForeignKey(ProductDeclination, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    description_for_buyers = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'product_declination_translation'
        unique_together = (('id', 'lang'),)


class ProductDeclinationVersion(models.Model):
    id = models.ForeignKey(ProductDeclination, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_for_buyers = models.TextField(blank=True, null=True)
    product_id = models.BigIntegerField()
    prioritary = models.NullBooleanField()
    use_stock = models.BooleanField()
    stock = models.BigIntegerField()
    stock_perfect = models.BigIntegerField()
    stock_critical = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'product_declination_version'
        unique_together = (('id', 'version', 'lang'),)


class ProductIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Product, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'product_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class ProductLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_link'


class ProductManifestationLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk = models.ForeignKey(Manifestation, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_manifestation_link'


class ProductMetaEventLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk = models.ForeignKey(MetaEvent, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_meta_event_link'


class ProductPriceLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_price_link'


class ProductProductLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_product_link'


class ProductTranslation(models.Model):
    id = models.ForeignKey(Product, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=127, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'product_translation'
        unique_together = (('id', 'lang'),)


class ProductVersion(models.Model):
    id = models.ForeignKey(Product, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=127, blank=True, null=True)
    meta_event_id = models.BigIntegerField(blank=True, null=True)
    product_category_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture_id = models.BigIntegerField(blank=True, null=True)
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    vat_id = models.BigIntegerField(blank=True, null=True)
    shipping_fees = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_fees_vat_id = models.BigIntegerField(blank=True, null=True)
    online = models.BooleanField()
    use_stock = models.BooleanField()
    online_limit = models.BigIntegerField()
    online_limit_per_transaction = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'product_version'
        unique_together = (('id', 'version', 'lang'),)


class ProductWorkspaceLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.BigIntegerField()
    fk = models.ForeignKey('Workspace', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_workspace_link'


class Professional(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    professional_type = models.ForeignKey('ProfessionalType', models.DO_NOTHING, blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    contact_email_no_newsletter = models.BooleanField()
    contact_email_npai = models.BooleanField()
    department = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'professional'


class ProfessionalArchive(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    professional_type = models.ForeignKey('ProfessionalType', models.DO_NOTHING, blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    contact_email_no_newsletter = models.BooleanField()
    contact_email_npai = models.BooleanField()
    department = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'professional_archive'


class ProfessionalBase(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    organism_id = models.BigIntegerField()
    contact_id = models.BigIntegerField()
    professional_type_id = models.BigIntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    contact_email_no_newsletter = models.BooleanField()
    contact_email_npai = models.BooleanField()
    department = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'professional_base'


class ProfessionalType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'professional_type'


class RawAccounting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    accounting_id = models.BigIntegerField(blank=True, null=True)
    order = models.ForeignKey(OrderTable, models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_accounting'


class RawAccountingVersion(models.Model):
    id = models.ForeignKey(RawAccounting, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    accounting_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    invoice_id = models.BigIntegerField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'raw_accounting_version'
        unique_together = (('id', 'version'),)


class RemoteAuthentication(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    ipaddress = models.CharField(max_length=255)
    active = models.BooleanField()
    salt = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'remote_authentication'
        unique_together = (('sf_guard_user', 'ipaddress'),)


class Seat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    seated_plan = models.ForeignKey('SeatedPlan', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    rank = models.BigIntegerField()
    x = models.BigIntegerField()
    y = models.BigIntegerField()
    diameter = models.BigIntegerField()
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seat'
        unique_together = (('seated_plan', 'name'),)


class SeatLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    seat1 = models.ForeignKey(Seat, models.DO_NOTHING, db_column='seat1')
    seat2 = models.ForeignKey(Seat, models.DO_NOTHING, db_column='seat2')

    class Meta:
        managed = False
        db_table = 'seat_link'


class SeatedPlan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    seat_diameter = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    picture = models.ForeignKey(Picture, models.DO_NOTHING, blank=True, null=True)
    online_picture = models.ForeignKey(Picture, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    background = models.CharField(max_length=255, blank=True, null=True)
    ideal_width = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seated_plan'


class SeatedPlanVersion(models.Model):
    id = models.ForeignKey(SeatedPlan, models.DO_NOTHING, db_column='id')
    seat_diameter = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    picture_id = models.BigIntegerField(blank=True, null=True)
    online_picture_id = models.BigIntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    background = models.CharField(max_length=255, blank=True, null=True)
    ideal_width = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'seated_plan_version'
        unique_together = (('id', 'version'),)


class SeatedPlanWorkspace(models.Model):
    id = models.BigIntegerField(primary_key=True)
    seated_plan = models.ForeignKey(SeatedPlan, models.DO_NOTHING)
    workspace = models.ForeignKey('Workspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seated_plan_workspace'


class SfGuardForgotPassword(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('SfGuardUser', models.DO_NOTHING)
    unique_key = models.CharField(max_length=255, blank=True, null=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_forgot_password'


class SfGuardGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_group'


class SfGuardGroupPermission(models.Model):
    group = models.ForeignKey(SfGuardGroup, models.DO_NOTHING)
    permission = models.ForeignKey('SfGuardPermission', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_group_permission'
        unique_together = (('group', 'permission'),)


class SfGuardPermission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_permission'


class SfGuardRememberKey(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('SfGuardUser', models.DO_NOTHING, blank=True, null=True)
    remember_key = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_remember_key'


class SfGuardUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=128)
    algorithm = models.CharField(max_length=128)
    salt = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    is_active = models.NullBooleanField()
    is_super_admin = models.NullBooleanField()
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_user'


class SfGuardUserGroup(models.Model):
    user = models.ForeignKey(SfGuardUser, models.DO_NOTHING)
    group = models.ForeignKey(SfGuardGroup, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_user_group'
        unique_together = (('user', 'group'),)


class SfGuardUserPermission(models.Model):
    user = models.ForeignKey(SfGuardUser, models.DO_NOTHING)
    permission = models.ForeignKey(SfGuardPermission, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_guard_user_permission'
        unique_together = (('user', 'permission'),)


class SlavePing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slave_ping'


class Survey(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    weight = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'


class SurveyAnswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    survey_query = models.ForeignKey('SurveyQuery', models.DO_NOTHING)
    survey_answers_group = models.ForeignKey('SurveyAnswersGroup', models.DO_NOTHING)
    lang = models.CharField(max_length=255)
    value = models.TextField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_answer'


class SurveyAnswerIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(SurveyAnswer, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'survey_answer_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class SurveyAnswerVersion(models.Model):
    id = models.ForeignKey(SurveyAnswer, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    survey_query_id = models.BigIntegerField()
    survey_answers_group_id = models.BigIntegerField()
    lang = models.CharField(max_length=255)
    value = models.TextField()
    contact_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'survey_answer_version'
        unique_together = (('id', 'version'),)


class SurveyAnswersGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    professional = models.ForeignKey(Professional, models.DO_NOTHING, blank=True, null=True)
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_answers_group'


class SurveyAnswersGroupVersion(models.Model):
    id = models.ForeignKey(SurveyAnswersGroup, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    survey_id = models.BigIntegerField()
    contact_id = models.BigIntegerField(blank=True, null=True)
    professional_id = models.BigIntegerField(blank=True, null=True)
    transaction_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'survey_answers_group_version'
        unique_together = (('id', 'version'),)


class SurveyApplyTo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(GroupTable, models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    professional = models.ForeignKey(Professional, models.DO_NOTHING, blank=True, null=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING, blank=True, null=True)
    everywhere = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_apply_to'


class SurveyApplyToVersion(models.Model):
    id = models.ForeignKey(SurveyApplyTo, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    survey_id = models.BigIntegerField()
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    manifestation_id = models.BigIntegerField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    contact_id = models.BigIntegerField(blank=True, null=True)
    professional_id = models.BigIntegerField(blank=True, null=True)
    organism_id = models.BigIntegerField(blank=True, null=True)
    everywhere = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'survey_apply_to_version'
        unique_together = (('id', 'version'),)


class SurveyIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(Survey, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'survey_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class SurveyQuery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    type = models.CharField(max_length=255)
    can_be_empty = models.BooleanField()
    weight = models.BigIntegerField()
    rank = models.BigIntegerField()
    stats = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_query'


class SurveyQueryIndex(models.Model):
    keyword = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    position = models.BigIntegerField()
    id = models.ForeignKey(SurveyQuery, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'survey_query_index'
        unique_together = (('keyword', 'field', 'position', 'id'),)


class SurveyQueryOption(models.Model):
    id = models.BigIntegerField(primary_key=True)
    survey_query = models.ForeignKey(SurveyQuery, models.DO_NOTHING)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'survey_query_option'


class SurveyQueryOptionTranslation(models.Model):
    id = models.ForeignKey(SurveyQueryOption, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=255)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'survey_query_option_translation'
        unique_together = (('id', 'lang'),)


class SurveyQueryTranslation(models.Model):
    id = models.ForeignKey(SurveyQuery, models.DO_NOTHING, db_column='id')
    name = models.TextField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'survey_query_translation'
        unique_together = (('id', 'lang'),)


class SurveyQueryVersion(models.Model):
    id = models.ForeignKey(SurveyQuery, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.TextField()
    survey_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    can_be_empty = models.BooleanField()
    weight = models.BigIntegerField()
    rank = models.BigIntegerField()
    stats = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'survey_query_version'
        unique_together = (('id', 'version', 'lang'),)


class SurveyTranslation(models.Model):
    id = models.ForeignKey(Survey, models.DO_NOTHING, db_column='id')
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'survey_translation'
        unique_together = (('id', 'lang'),)


class SurveyVersion(models.Model):
    id = models.ForeignKey(Survey, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'survey_version'
        unique_together = (('id', 'version', 'lang'),)


class Tax(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.FloatField()
    with_shipment = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class TaxManifestation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tax_id = models.BigIntegerField()
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tax_manifestation'


class TaxPrice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tax = models.ForeignKey(Tax, models.DO_NOTHING)
    price_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tax_price'


class TaxUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tax = models.ForeignKey(Tax, models.DO_NOTHING)
    sf_guard_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tax_user'


class TaxVersion(models.Model):
    id = models.ForeignKey(Tax, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.FloatField()
    with_shipment = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tax_version'
        unique_together = (('id', 'version'),)


class Ticket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    transaction = models.ForeignKey('Transaction', models.DO_NOTHING)
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    manifestation = models.ForeignKey(Manifestation, models.DO_NOTHING)
    gauge = models.ForeignKey(Gauge, models.DO_NOTHING)
    price = models.ForeignKey(Price, models.DO_NOTHING, blank=True, null=True)
    price_name = models.CharField(max_length=63)
    seat = models.ForeignKey(Seat, models.DO_NOTHING, blank=True, null=True)
    duplicating = models.ForeignKey('self', models.DO_NOTHING, db_column='duplicating', blank=True, null=True)
    grouping_fingerprint = models.CharField(max_length=255, blank=True, null=True)
    cancelling = models.ForeignKey('self', models.DO_NOTHING, db_column='cancelling', blank=True, null=True)
    printed_at = models.DateTimeField(blank=True, null=True)
    integrated_at = models.DateTimeField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    othercode = models.CharField(max_length=255, blank=True, null=True)
    member_card = models.ForeignKey(MemberCard, models.DO_NOTHING, blank=True, null=True)
    taxes = models.DecimalField(max_digits=6, decimal_places=3)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    auto_by_hold = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'
        unique_together = (('seat', 'manifestation'),)


class TicketVersion(models.Model):
    id = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    transaction_id = models.BigIntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=4)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    manifestation_id = models.BigIntegerField()
    gauge_id = models.BigIntegerField()
    price_id = models.BigIntegerField(blank=True, null=True)
    price_name = models.CharField(max_length=63)
    seat_id = models.BigIntegerField(blank=True, null=True)
    duplicating = models.BigIntegerField(blank=True, null=True)
    grouping_fingerprint = models.CharField(max_length=255, blank=True, null=True)
    cancelling = models.BigIntegerField(blank=True, null=True)
    printed_at = models.DateTimeField(blank=True, null=True)
    integrated_at = models.DateTimeField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    othercode = models.CharField(max_length=255, blank=True, null=True)
    member_card_id = models.BigIntegerField(blank=True, null=True)
    taxes = models.DecimalField(max_digits=6, decimal_places=3)
    contact_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    auto_by_hold = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ticket_version'
        unique_together = (('id', 'version'),)


class Traceable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traceable'


class TraceableVersion(models.Model):
    id = models.ForeignKey(Traceable, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'traceable_version'
        unique_together = (('id', 'version'),)


class Transaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    professional = models.ForeignKey(Professional, models.DO_NOTHING, blank=True, null=True)
    transaction = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255)
    closed = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    send_an_email = models.BooleanField()
    deposit = models.BooleanField()
    with_shipment = models.BooleanField()
    postalcode = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'


class TransactionVersion(models.Model):
    id = models.ForeignKey(Transaction, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    contact_id = models.BigIntegerField(blank=True, null=True)
    professional_id = models.BigIntegerField(blank=True, null=True)
    transaction_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255)
    closed = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    send_an_email = models.BooleanField()
    deposit = models.BooleanField()
    with_shipment = models.BooleanField()
    postalcode = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_version'
        unique_together = (('id', 'version'),)


class TypeOfResources(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_of_resources'


class UserPrice(models.Model):
    price = models.ForeignKey(Price, models.DO_NOTHING)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_price'
        unique_together = (('price', 'sf_guard_user'), ('sf_guard_user', 'price'),)


class Vat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=5, decimal_places=4)
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vat'


class VatVersion(models.Model):
    id = models.ForeignKey(Vat, models.DO_NOTHING, db_column='id')
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=5, decimal_places=4)
    accounting_account = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vat_version'
        unique_together = (('id', 'version'),)


class WebOrigin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING, blank=True, null=True)
    automatic = models.BooleanField()
    first_page = models.TextField()
    ipaddress = models.CharField(max_length=40)
    referer = models.TextField(blank=True, null=True)
    campaign = models.TextField(blank=True, null=True)
    transaction = models.ForeignKey(Transaction, models.DO_NOTHING)
    user_agent = models.TextField()
    next = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_origin'


class WebOriginIp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ipaddress = models.CharField(max_length=40)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'web_origin_ip'


class WebOriginVersion(models.Model):
    id = models.ForeignKey(WebOrigin, models.DO_NOTHING, db_column='id')
    sf_guard_user_id = models.BigIntegerField(blank=True, null=True)
    automatic = models.BooleanField()
    first_page = models.TextField()
    ipaddress = models.CharField(max_length=40)
    referer = models.TextField(blank=True, null=True)
    campaign = models.TextField(blank=True, null=True)
    transaction_id = models.BigIntegerField()
    user_agent = models.TextField()
    next_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'web_origin_version'
        unique_together = (('id', 'version'),)


class Workspace(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    on_ticket = models.CharField(max_length=255, blank=True, null=True)
    seated = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'workspace'


class WorkspacePrice(models.Model):
    price = models.ForeignKey(Price, models.DO_NOTHING)
    workspace = models.ForeignKey(Workspace, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_price'
        unique_together = (('workspace', 'price'), ('price', 'workspace'),)


class WorkspaceUser(models.Model):
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING)
    workspace = models.ForeignKey(Workspace, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'workspace_user'
        unique_together = (('sf_guard_user', 'workspace'),)


class WorkspaceUserOrdering(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sf_guard_user = models.ForeignKey(SfGuardUser, models.DO_NOTHING)
    workspace = models.ForeignKey(Workspace, models.DO_NOTHING)
    rank = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'workspace_user_ordering'
        unique_together = (('sf_guard_user', 'workspace'),)


class YOB(models.Model):
    id = models.BigIntegerField(primary_key=True)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    day = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'y_o_b'
