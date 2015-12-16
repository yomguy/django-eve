#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

import datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.mail import send_mail

from presta.models import PsCustomer
from eve.models import Contact
from eve.utils import Logger
from eve.views import Presta2Eve


class Command(BaseCommand):

    help = "Copy/Update contacts from a PrestaShop DB into a E-venement DB"

    mail_from = 'guillame.pellerin@ircam.fr'
    mail_to = 'caroline.palmier@ircam.fr'

    test_customers = ['julie.pak@gmail.com',
                        'remi.test@gmail.com',
                        'marie.testa@hotmail.fr',
                        'bernard.testabel@ircam.fr',
                        'jean.testarin@testeasy.com',
                        'marie.lunette@testoptique.com',
                        'pierre.foot@testobut.com',
                        'atorrino@tasty.com',
                        'axel.rose@gunsnroses.com',
                        'paul.stanley@kiss.com',
                        'd.grohl@foofighters.com',
                        't.dernier@cite-musique.fr']

    option_list = BaseCommand.option_list + (
          make_option('-l', '--log',
            dest='log',
            help='define log file'),
          make_option('-t', '--test',
            action='store_true',
            dest='test',
            help='only process test customers'),
          make_option('-u', '--update',
            action='store_true',
            dest='update',
            help='update customer dates'),
          )

    def handle(self, *args, **kwargs):
        start_time = datetime.datetime.now()
        log_file = kwargs.get('log')
        test =  kwargs.get('test')
        update =  kwargs.get('update')
        logger = Logger(log_file)
        new_contacts = 0
        updated_contacts = 0
        contacts = Contact.objects.all()
        force = test
        
        if test:
            customers = []
            for email in self.test_customers:
                customers.append(PsCustomer.objects.get(email=email))
            n_customers = len(customers)
        else:
            customers = PsCustomer.objects.all()
            n_customers = customers.count()

        for customer in customers:
            if update:
                customer.date_upd = datetime.datetime.now()
                customer.save()
            p2e = Presta2Eve(customer, logger, force)
            p2e.run()
            if p2e.contact_created:
                new_contacts += 1
            elif p2e.contact_updated:
                updated_contacts += 1

        logger.logger.info('*********************************************************')
        logger.logger.info('Total PrestaShop treated customers : ' + str(n_customers))
        logger.logger.info('Total E-venement existing contacts : ' + str(contacts.count()))
        logger.logger.info('Total E-venement created contacts : ' + str(new_contacts))
        logger.logger.info('Total E-venement updated contacts : ' + str(updated_contacts))
        logger.logger.info('*********************************************************')
