#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('README.rst') as file:
    long_description = file.read()


setup(
    name='BASC-Archiver',
    version='0.8.0',
    description='Makes a complete archive of imageboard threads including images, HTML, and JSON.',
    long_description=long_description,
    author='Lawrence Wu <sagnessagiel@gmail.com>, Daniel Oaks <daniel@danieloaks.net>',
    author_email='sagnessagiel@gmail.com',
    url='https://github.com/DanielOaks/BASC-Archiver',
    packages=['basc_archiver', 'basc_archiver.sites'],
    package_dir={
        'basc_archiver': 'basc_archiver',
        'basc_archiver.sites': 'basc_archiver/sites',
    },
    install_requires=['requests', 'docopt==0.5.0', 'py-4chan'],
    keywords='4chan downloader images json dump',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
