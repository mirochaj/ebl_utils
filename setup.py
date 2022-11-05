#!/usr/bin/env python
from __future__ import print_function
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ebl_utils',
      version='0.1',
      description='EBL utilities',
      author='Jordan Mirocha',
      author_email='mirochaj@gmail.com',
      url='https://github.com/mirochaj/ebl_utils',
      packages=['ebl_utils'],
     )
