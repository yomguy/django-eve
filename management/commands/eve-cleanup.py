#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from eve.models import *


class Command(BaseCommand):

    help = "Cleanup Eve DB"

    def handle(self, *args, **kwargs):
        contacts = Contact.objects.filter(email__contains='npai_')
        for contact in contacts:
            print contact.email
            contact.email = contact.email.replace('npai_', '')
            contact.email_npai = True
            contact.save()

        contacts = Contact.objects.filter(email__contains='_npai')
        for contact in contacts:
            print contact.email
            contact.email = contact.email.replace('_npai', '')
            contact.email_npai = True
            contact.save()

        contacts = Contact.objects.filter(email__contains='ddm_')
        for contact in contacts:
            print contact.email
            contact.email = contact.email.replace('ddm_', '')
            contact.email_no_newsletter = True
            contact.save()

        contacts = Contact.objects.filter(email__contains='_ddm')
        for contact in contacts:
            print contact.email
            contact.email = contact.email.replace('_ddm', '')
            contact.email_no_newsletter = True
            contact.save()
