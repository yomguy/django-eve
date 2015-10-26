#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

from django.shortcuts import render

import re
from eve.models import *
from presta.models import *


class Presta2Eve(object):
    """Data migrator between PrestaShop and E-venement"""

    default_lang = 'fr'

    def __init__(self, customer, logger=None, dry_run=False):
        self.customer = customer
        self.professional = None
        self.organism = None
        self.addresss = ''
        self.dry_run = dry_run
        self.test_group_id = 40
        self.forum_group_id = 39
        if not logger:
            logger = Logger('/tmp/presta2eve.log')
        self.logger = logger.logger

    def get_contact(self):
        contacts = Contact.objects.filter(email=self.customer.email)
        names, domain = self.customer.email.split('@')

        if contacts:
            self.contact = contacts[0]
            self.contact_created = False
            # self.set_version()
        else:
            emails = [ name + '@' + domain for name in names.split('.')]
            for name in names.split('.'):
                email = name.capitalize() + '@' + domain
                if not email in emails:
                    emails.append(email)
                email = name.lower() + '@' + domain
                if not email in emails:
                    emails.append(email)
            contacts = None
            for email in emails:
                contacts = Contact.objects.filter(email=email)
                if contacts:
                    self.contact = contacts[0]
                    self.contact_created = False
                    break
            if not contacts:
                self.contact = Contact(email=self.customer.email)
                self.contact_created = True

    def set_contact(self):
        if self.customer.lastname:
            self.contact.name = self.contact.name or self.customer.lastname.capitalize()
            self.contact.description = 'PRESTA ' + str(self.customer.id_customer)
        else:
            self.contact.name = 'PRESTA ' + str(self.customer.id_customer)
        self.contact.firstname = self.contact.firstname or self.customer.firstname.capitalize()
        self.contact.confirmed = True

        if not self.dry_run:
            self.contact.save()

        if self.contact_created:
            self.logger.info('contact created : ' + str(self.contact.id))
        else:
            self.logger.info('contact updated : ' + str(self.contact.id))

    def set_version(self):
        versions = ContactVersion.objects.filter(id=self.contact).order_by('-version')
        if versions:
            num = versions[0].version + 1
        else:
            num = 1
        version = ContactVersion()
        for field in self.contact._meta.fields:
            if not field.name == 'id':
                setattr(version, field.name, getattr(self.contact, field.name))
        if not self.dry_run:
            version.id = self.contact
            version.version = num
            version.save()

        self.logger.info('version added')

    def set_index(self):
        if self.contact_created:
            index, c = ContactIndex.objects.get_or_create(id=self.contact, field='name', keyword=self.contact.name, position=0L)
            if self.contact.firstname:
                index, c = ContactIndex.objects.get_or_create(id=self.contact, field='firstname', keyword=self.contact.firstname, position=1L)
            i = 2
            keywords = re.split('\.|\@', self.contact.email)
            for keyword in keywords:
                if keyword:
                    try:
                        index, c = ContactIndex.objects.get_or_create(id=self.contact, field='email', keyword=keyword, position=i)
                    except:
                        pass
                    i += 1

            self.logger.info('index updated')

    def set_lang(self):
        if self.customer.id_lang:
            self.ps_lang = PsLang.objects.get(id_lang=self.customer.id_lang)
        else:
            self.ps_lang = PsLang.objects.get(iso_code=self.default_lang)
        self.contact.culture = self.ps_lang.name

        if not self.dry_run:
            self.contact.save()

        self.logger.info('culture updated')

    def set_gender(self):
        if self.customer.id_gender == 1 and self.ps_lang.iso_code == 'fr':
            self.contact.title = 'Monsieur'
        elif self.customer.id_gender == 1 and self.ps_lang.iso_code == 'en':
            self.contact.title = 'Mr.'
        elif self.customer.id_gender == 2 and self.ps_lang.iso_code == 'fr':
            self.contact.title = 'Madame'
        elif self.customer.id_gender == 1 and self.ps_lang.iso_code == 'en':
            self.contact.title = 'Mrs.'

        if not self.dry_run:
            self.contact.save()

        self.logger.info('genre updated')

    def set_address(self):
        self.ps_addresses = PsAddress.objects.filter(id_customer=self.customer.id_customer, deleted=0)
        if not self.ps_addresses:
            self.ps_address = ''
            self.logger.info('no address')
        else:
            self.ps_address = self.ps_addresses[0]
            self.address = self.ps_address.address1 + '\n' + self.ps_address.address2

            if len(self.ps_addresses) > 1:
                #TODO: get livraison ?
                self.logger.info('more than 1 address')

            self.contact.address = self.address
            self.contact.postalcode = self.ps_address.postcode
            self.contact.city = self.ps_address.city

            if self.ps_address.id_country:
                self.country = PsCountryLang.objects.get(id_country=self.ps_address.id_country, id_lang=self.ps_lang.id_lang).name
                self.contact.country = self.country
            else:
                self.contact.country = None

            if not self.dry_run:
                self.contact.save()

            self.logger.info('address updated')

    def set_phonenumber(self):
        if self.ps_address:
            phone_numbers = ContactPhonenumber.objects.filter(contact=self.contact)
            if phone_numbers:
                if len(phone_numbers) > 1:
                    self.logger.info('has more than 1 phone number')
                phone_number = phone_numbers[0]
            else:
                phone_number = ContactPhonenumber(contact=self.contact)
            #TODO: type

            number = self.ps_address.phone_mobile.replace(' ', '')
            n = 2
            number = ' '.join([number[i:i+n] for i in range(0, len(number), n)])
            if phone_number.number != number:
                phone_number.number = number
                if not self.dry_run:
                    phone_number.save()

                self.logger.info('phone updated')

    def set_birthday(self):
        if self.customer.birthday:
            yobs = YOB.objects.filter(contact=self.contact)
            if yobs:
                yob = yob[0]
            else:
                yob = YOB(contact=self.contact)
            yob.year = self.customer.birthday.year
            yob.month = self.customer.birthday.month
            yob.day = self.customer.birthday.day

            if not self.dry_run:
                yob.save()

            self.logger.info('birthday updated')

    def set_organism(self):
        custom_field = PsCustomField.objects.get(id_custom_field=2)
        ps_organisms = PsCustomerCustomFieldValue.objects.filter(id_customer=self.customer, id_custom_field=custom_field)
        if ps_organisms:
            ps_organism = ps_organisms[0]
            organisms = Organism.objects.filter(name=ps_organism.value)
            if not organisms:
                self.organism = Organism(name=ps_organism.value)
            else:
                self.organism = organisms[0]

            if self.ps_addresses:
                self.organism.address = self.organism.address or self.contact.address
                self.organism.postalcode = self.organism.postalcode or self.contact.postalcode
                self.organism.city = self.organism.city or self.contact.city
                self.organism.country = self.organism.country or self.contact.country

            if not self.dry_run:
                self.organism.save()

            self.logger.info('organism updated')

    def set_professional(self):
        if self.organism:
            professionals = Professional.objects.filter(organism=self.organism, contact=self.contact)
            if not professionals:
                self.professional = Professional(organism=self.organism, contact=self.contact)
                self.professional.contact_email = self.contact.email
                self.professional.name = self.professional.name or self.contact.name
                #TODO: phone, etc..

                if not self.dry_run:
                    self.professional.save()

                self.logger.info('professional updated')

    def add_contact_to_group(self, group_id):
        group = GroupTable.objects.get(id=group_id)
        group_contact, c = GroupContact.objects.get_or_create(contact=self.contact, group=group)
        if self.professional:
            self.add_professional_to_group(group_id)
        if c:
            self.logger.info('contact added to group : ' + group.name)

    def remove_contact_from_group(self, group_id):
        group = GroupTable.objects.get(id=group_id)
        groups = GroupContact.objects.filter(contact=self.contact, group=group)
        for g in groups:
            g.delete()
            self.logger.info('contact group deleted : ' + group.name)
        if self.professional:
            self.remove_professional_from_group(group_id)

    def add_professional_to_group(self, group_id):
        group = GroupTable.objects.get(id=group_id)
        group_professional, c = GroupProfessional.objects.get_or_create(professional=self.professional, group=group)
        if c:
            self.logger.info('professional added to group : ' + group.name)

    def remove_professional_from_group(self, group_id):
        group = GroupTable.objects.get(id=group_id)
        groups = GroupProfessional.objects.filter(professional=self.professional, group=group)
        for g in groups:
            g.delete()
            self.logger.info('professional group deleted : ' + group.name)

    def set_groups(self):
        ps_groups = PsCustomerGroup.objects.filter(id_customer=self.customer.id_customer)
        ps_groups_ids = [ps_group.id_group for ps_group in ps_groups]

        def add_excluding_group_11(id):
            if len(ps_groups) == 1:
                if not ps_groups[0].id_group == 11:
                    self.add_contact_to_group(id)
            else:
                self.add_contact_to_group(id)

        def is_in_group(id):
            return id in ps_groups_ids

        def is_forum():
            return is_in_group(self.forum_group_id)

        def is_test():
            return is_in_group(self.test_group_id)

        add_excluding_group_11(393)

        if is_forum():
            self.add_contact_to_group(4)
        else:
            add_excluding_group_11(4)

        if is_forum():
            self.add_contact_to_group(5)
        else:
            add_excluding_group_11(5)

        if self.professional:
            add_excluding_group_11(390)

        if 13 in ps_groups_ids or 14 in ps_groups_ids or 15 in ps_groups_ids:
            self.add_contact_to_group(457)

        group = GroupTable.objects.get(id=457)
        groups = GroupContact.objects.filter(contact=self.contact, group=group)
        if not (13 in ps_groups_ids or 14 in ps_groups_ids or 15 in ps_groups_ids) and groups:
            self.remove_contact_from_group(457)
            self.add_contact_to_group(458)

        if 25 in ps_groups_ids or 35 in ps_groups_ids:
            self.add_contact_to_group(459)

        if is_forum() and len(ps_groups) == 1 and 11 in ps_groups_ids:
            self.add_contact_to_group(46)

        if not is_forum() and 38 in ps_groups_ids:
            self.add_contact_to_group(460)

    def run(self):
        self.get_contact()
        if self.contact_created or (self.contact.updated_at and self.contact.updated_at < self.customer.date_upd):
            self.logger.info('*********************************************************')
            self.logger.info(self.customer.lastname)
            self.logger.info(self.customer.email)
            self.logger.info(self.customer.id_customer)
            self.set_contact()
            # self.set_version()
            self.set_index()
            self.set_lang()
            self.set_gender()
            self.set_address()
            self.set_phonenumber()
            self.set_birthday()
            self.set_organism()
            self.set_professional()
            self.set_groups()
