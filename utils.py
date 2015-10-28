#!/usr/bin/python
# Copyright (C) 2015 Guillaume Pellerin <guillaume.pellerin@ircam.fr>
# Licence: MIT


import logging

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
        from auditlog.models import LogEntry
        self.log = open(path + '.audit', 'w')
        self.start_time = start_time

    def write(self):
        logs = LogEntry.objects.filter(timestamp__gte=self.start_time)
        for log in logs:
            self.log.write('\n' + log.timestamp.__str__())
            self.log.write(log.object_repr)
            self.log.write('\n')
            self.log.write(str(log.object_id) + ' : ')
            self.log.write(log.changes_str.encode('utf8'))
        self.log.close()
