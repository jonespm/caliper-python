#!/usr/bin/env python3
import re

from io import open
from setuptools import setup
from os import path

_packages = ['caliper', 'caliper.util']
_test_requirements = ['flake8', 'pytest', 'pytest-cov', 'responses', 'tox']

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as fd:
    _install_requirements = fd.read().splitlines()

with open(path.join(here, 'README.md'), encoding='utf-8') as fd:
    _readme = fd.read()


def _get_val_from_mod(k):
    with open(path.join(here, 'caliper', '__init__.py'), encoding='utf-8') as fd:
        return re.search(r'^__{0}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(k), fd.read(),
                         re.MULTILINE).group(1)


_author = _get_val_from_mod('author')
_license = _get_val_from_mod('license')
_title = _get_val_from_mod('title')
_version = _get_val_from_mod('version')

setup(
    name=_title,
    version=_version,
    description='Caliper API for Python. Provides implementation for the IMS Caliper Sensor API.',
    long_description=_readme + '\n\n',
    long_description_content_type='text/markdown',
    url='https://github.com/IMSGlobal/caliper-python',
    author=_author,
    author_email='info@imsglobal.org',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=_packages,
    python_requires='>=3',
    install_requires=_install_requirements,
    extras_require={
        'dev': _test_requirements,
        'test': _test_requirements
    },
    project_urls={
        'Homepage': 'https://www.imsglobal.org/activity/caliper',
        'Source': 'https://github.com/IMSGlobal/caliper-python',
        'Tracker': 'https://github.com/IMSGlobal/caliper-python/issues'
    })
