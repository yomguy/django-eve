#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

setup(
    name='django-eve',
    url='https://forge.ircam.fr/p/django-eve/',
    description="Django module implementing the E-venement models (needed for Passerelle & co @IRCAM)",
    long_description=open('README.rst').read(),
    author="Guillaume Pellerin",
    author_email="guillaume.pellerin@ircam.fr",
    version='1.0',
    install_requires=['django',],
    platforms=['OS Independent'],
    license='Gnu Public License V3',
    packages=['eve'],
    include_package_data=True,
    zip_safe=False,
    )
