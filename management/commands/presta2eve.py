#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

import datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from presta.models import PsCustomer
from eve.utils import Logger, AuditLogger
from eve.views import Presta2Eve


class Command(BaseCommand):

    help = "Copy/Update contacts from a PrestaShop DB into a E-venement DB"

    option_list = BaseCommand.option_list + (
          make_option('-d', '--dry-run',
            action='store_true',
            dest='dry_run',
            help='Do NOT write anything'),
          make_option('-l', '--log',
            dest='log',
            help='define log file'),
          make_option('-n', '--number',
            dest='number',
            help='set maximum number of loops'),
          )

    def handle(self, *args, **kwargs):
        start_time = datetime.datetime.now()
        log_file = kwargs.get('log')
        dry_run =  kwargs.get('dry_run')
        n = kwargs.get('number')
        logger = Logger(log_file)
        if n:
            n = int(n)

        i = 0
        customers = PsCustomer.objects.all()
        for customer in customers:
            p2e = Presta2Eve(customer, logger, dry_run)
            p2e.run()
            if n and i >= n:
                break
            i+= 1

        audit_logger = AuditLogger(log_file + '.audit', start_time)
        audit_logger.write()
