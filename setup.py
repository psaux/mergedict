#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import codecs
from setuptools import setup

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', 'utf8',
) as ld_file:
    long_description = ld_file.read()


install_requires = []
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    install_requires.append('singledispatch')

setup (
    name = 'mergedict',
    version = '0.2.0',
    author = 'Eduardo Naufel Schettino',
    author_email = 'schettino72@gmail.com',
    description = 'A Python `dict` with a merge() method.',
    long_description = long_description,
    url = 'https://github.com/schettino72/mergedict/',
    keywords = ['dict', 'singledispatch', 'config'],
    platforms = ['any'],
    license = 'MIT',
    py_modules = ['mergedict'],
    install_requires = install_requires,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
