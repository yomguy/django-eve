#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

import datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from presta.models import PsCustomer
from eve.utils import Logger
from eve.views import Presta2Eve


class Command(BaseCommand):

    help = "Copy/Update contacts from a PrestaShop DB into a E-venement DB"

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
                        'd.grohl@foofighters.com']

    option_list = BaseCommand.option_list + (
          make_option('-d', '--dry-run',
            action='store_true',
            dest='dry_run',
            help='Do NOT write anything'),
          make_option('-l', '--log',
            dest='log',
            help='define log file'),
          make_option('-t', '--test',
            action='store_true',
            dest='test',
            help='only process test customers'),
          )

    def handle(self, *args, **kwargs):
        start_time = datetime.datetime.now()
        log_file = kwargs.get('log')
        dry_run =  kwargs.get('dry_run')
        test =  kwargs.get('test')
        logger = Logger(log_file)

        if test:
            customers = []
            for email in self.test_customers:
                customers.append(PsCustomer.objects.get(email=email))
        else:
            customers = PsCustomer.objects.all()

        for customer in customers:
            p2e = Presta2Eve(customer, logger, dry_run)
            p2e.run()

        try:
            from eve.utils import AuditLogger
            audit_logger = AuditLogger(log_file + '.audit', start_time)
            audit_logger.write()
        except:
            pass
