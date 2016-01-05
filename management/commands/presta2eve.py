#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

import os, datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from presta.models import PsCustomer
from eve.models import Contact
from eve.utils import Logger
from eve.views import Presta2Eve


class Command(BaseCommand):

    help = "Copy/Update contacts from a PrestaShop DB into a E-venement DB"

    from_email = 'guillame.pellerin@ircam.fr'
    # to_email = ['caroline.palmier@ircam.fr', 'guillame.pellerin@ircam.fr']
    to_email = ['yomguy@localhost',]

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
          make_option('-l', '--log_dir',
            dest='log_dir',
            help='define log dir'),
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
        log_dir = kwargs.get('log_dir')
        test =  kwargs.get('test')
        update =  kwargs.get('update')
        new_contacts = 0
        updated_contacts = 0
        contacts = Contact.objects.all()
        force = test

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        date = datetime.datetime.now()
        log_filename = 'presta2eve_' + date.isoformat() + '.log'
        log_file = os.path.abspath(os.path.join(log_dir, log_filename))
        logger = Logger(log_file)

        if test:
            customers = []
            for email in self.test_customers:
                try:
                    customer = PsCustomer.objects.get(email=email)
                    customers.append(customer)
                except:
                    pass
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

        email = EmailMessage(subject='Presta2Eve logger', body='The log file is in attachment.',
                    from_email=self.from_email, to=self.to_email)
        email.attach_file(log_file, 'text/plain')
        email.send()
