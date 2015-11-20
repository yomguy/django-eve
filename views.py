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

    def __init__(self, customer, logger=None):
        self.customer = customer
        self.professional = None
        self.organism = None
        self.addresss = ''
        self.test_group_id = 40
        self.forum_group_id = 39
        self.default_group_id = 11
        self.is_elligible = True
        if not logger:
            logger = Logger('/tmp/presta2eve.log')
        self.logger = logger.logger

    def get_groups(self):
        self.ps_groups = PsCustomerGroup.objects.filter(id_customer=self.customer.id_customer)
        self.ps_groups_ids = [ps_group.id_group for ps_group in self.ps_groups]

        # cleanup Test and Forum group
        self.is_forum = False
        if self.forum_group_id in self.ps_groups_ids:
            self.is_forum = True
            self.ps_groups_ids.remove(self.forum_group_id)

        self.is_test = False
        if self.test_group_id in self.ps_groups_ids:
            self.is_test = True
            self.ps_groups_ids.remove(self.test_group_id)

        if len(self.ps_groups_ids) == 1 and self.default_group_id in self.ps_groups_ids:
            self.is_elligible = False

    def get_contact(self):
        contacts = Contact.objects.filter(email=self.customer.email)
        professionals = Professional.objects.filter(contact_email=self.customer.email)
        organisms = Organism.objects.filter(email=self.customer.email)
        names, domain = self.customer.email.split('@')

        if contacts:
            self.contact = contacts[0]
            self.contact_created = False
            # self.set_version()
        elif professionals:
            if organisms:
                self.organism = organisms[0]
                self.professional = self.organisms.professional
                self.contact = self.professional.contact
                if self.professional.contact_email:
                    self.contact.email = self.professional.contact_email
                else:
                    self.contact.email = self.organism.email
            else:
                self.professional = professionals[0]
                self.contact = self.professional.contact
                self.contact.email = self.professional.contact_email
            self.contact_created = False
            self.contact.save()
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
        if self.contact.description:
            self.contact.description = self.contact.description + '\n' + 'PRESTA ' + str(self.customer.id_customer)
        else:
            self.contact.description = 'PRESTA ' + str(self.customer.id_customer)
        if self.customer.lastname:
            self.contact.name = self.contact.name or self.customer.lastname.upper()
        else:
            self.contact.name = 'PRESTA ' + str(self.customer.id_customer)
        self.contact.firstname = self.contact.firstname or self.customer.firstname.capitalize()
        self.contact.confirmed = True
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
        version.id = self.contact
        version.version = num
        version.save()
        self.logger.info('version added')

    def create_index(self, field, keyword, position=0L):
        index, c = ContactIndex.objects.get_or_create(id=self.contact, field=field, keyword=keyword, position=position)

    def set_index(self):
        if self.contact_created:
            self.create_index(field='name', keyword=self.contact.name)
            if self.contact.firstname:
                self.create_index(field='firstname', keyword=self.contact.firstname)
            keywords = re.split('\.|\@', self.contact.email)
            position = 0L
            for keyword in keywords:
                if keyword:
                    self.create_index(field='email', keyword=keyword, position=position)
                    position += 1L
            self.logger.info('index updated')

    def set_lang(self):
        if self.customer.id_lang:
            self.ps_lang = PsLang.objects.get(id_lang=self.customer.id_lang)
        else:
            self.ps_lang = PsLang.objects.get(iso_code=self.default_lang)
        self.contact.culture = self.contact.culture or self.ps_lang.name
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
                self.logger.info('more than 1 address')

            if self.address:
                self.contact.address = self.address
                self.contact.city = self.ps_address.city.upper()
            if self.ps_address.postcode:
                self.contact.postalcode = self.ps_address.postcode

            if self.ps_address.id_country:
                self.country = PsCountryLang.objects.get(id_country=self.ps_address.id_country, id_lang=self.ps_lang.id_lang).name
                if self.country:
                    self.contact.country = self.country.upper()
            else:
                self.contact.country = None

            self.contact.save()
            self.logger.info('address updated')

    def set_phonenumber(self):
        n = 2
        if self.ps_address:
            if self.ps_address.phone:
                number = self.ps_address.phone.replace(' ', '')
                number = ' '.join([number[i:i+n] for i in range(0, len(number), n)])
                phone, c = ContactPhonenumber.objects.get_or_create(contact=self.contact, number=number, name='Fixe')
                self.logger.info('phone updated')

                number = self.ps_address.phone_mobile.replace(' ', '')
                number = ' '.join([number[i:i+n] for i in range(0, len(number), n)])
            if self.ps_address.phone_mobile:
                phone, c = ContactPhonenumber.objects.get_or_create(contact=self.contact, number=self.ps_address.phone_mobile, name='Mobile')
                self.logger.info('mobile phone updated')

    def set_birthday(self):
        if self.customer.birthday:
            yobs = YOB.objects.filter(contact=self.contact)
            if yobs:
                yob = yobs[0]
                self.logger.info('birthday selected')
            else:
                yob = YOB(contact=self.contact)
            yob.year = self.customer.birthday.year
            yob.month = self.customer.birthday.month
            yob.day = self.customer.birthday.day
            yob.save()
            self.logger.info('birthday updated')

    def set_organism(self):
        custom_field = PsCustomField.objects.get(id_custom_field=2)
        ps_organisms = PsCustomerCustomFieldValue.objects.filter(id_customer=self.customer, id_custom_field=custom_field)
        if ps_organisms:
            ps_organism = ps_organisms[0]
            if ps_organism.value:
                organisms = Organism.objects.filter(name=ps_organism.value)
                if not organisms:
                    organisms = Organism.objects.filter(name__contains=ps_organism.value)
                    if organisms:
                        if len(organisms) == 1:
                            self.organism = organisms[0]
                            self.logger.info('organism selected')
                        else:
                            self.logger.info('organism NOT SELECTED')
                    else:
                        self.organism = Organism(name=ps_organism.value)
                        if self.ps_addresses:
                            self.organism.address = self.contact.address
                            self.organism.postalcode = self.contact.postalcode
                            self.organism.city = self.contact.city
                            self.organism.country = self.contact.country
                            self.organism.save()
                            self.logger.info('organism created')
                else:
                    self.organism = organisms[0]
                    self.logger.info('organism selected')

    def set_professional(self):
        if self.organism:
            professionals = Professional.objects.filter(organism=self.organism, contact=self.contact)
            if not professionals:
                self.professional = Professional(organism=self.organism, contact=self.contact)
                self.professional.contact_email = self.professional.contact_email or self.contact.email
                self.professional.save()
                self.logger.info('professional created')
            else:
                self.professional = professionals[0]
                self.logger.info('professional selected')

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
        self.add_contact_to_group(393)
        self.add_contact_to_group(4)
        self.add_contact_to_group(5)

        if self.professional or self.organism:
            self.add_contact_to_group(390)

        if 13 in self.ps_groups_ids or 14 in self.ps_groups_ids or 15 in self.ps_groups_ids:
            self.add_contact_to_group(457)

        group = GroupTable.objects.get(id=457)
        groups = GroupContact.objects.filter(contact=self.contact, group=group)
        if not (13 in self.ps_groups_ids or 14 in self.ps_groups_ids or 15 in self.ps_groups_ids) and groups:
            self.remove_contact_from_group(457)
            self.add_contact_to_group(458)

        if 25 in self.ps_groups_ids or 35 in self.ps_groups_ids:
            self.add_contact_to_group(459)

        if self.is_forum and len(self.ps_groups_ids) == 1 and 11 in self.ps_groups_ids:
            self.add_contact_to_group(46)

        if not self.is_forum and 38 in self.ps_groups_ids:
            self.add_contact_to_group(460)

    def run(self):
        self.get_groups()
        self.get_contact()
        if (self.contact_created or (self.contact.updated_at and self.contact.updated_at < self.customer.date_upd)) and self.is_elligible:
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
        else:
            print self.contact.email, self.contact.updated_at, self.customer.date_upd
