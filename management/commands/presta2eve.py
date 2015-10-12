#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT

import logging, datetime
from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from presta.models import PsCustomer
from eve.views import Presta2Eve


class Logger:

    def __init__(self, file):
        self.logger = logging.getLogger('myapp')
        self.hdlr = logging.FileHandler(file)
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.INFO)


class AuditLogger(object):

    def __init__(self, path, start_time):
        self.log = open(path + '.audit', 'w')
        self.start_time = start_time

    def write(self):
        from auditlog.models import LogEntry
        logs = LogEntry.objects.filter(timestamp__gte=self.start_time)
        for log in logs:
            self.log.write('\n' + log.timestamp.__str__())
            self.log.write(' : ' + log.object_repr + ' ' + str(log.object_id) + ' : ')
            self.log.write(log.changes_str.encode('utf8'))
        self.log.close()



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
