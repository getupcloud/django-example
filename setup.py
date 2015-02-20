#!/usr/bin/env python

from setuptools import setup
import sys

if (sys.version_info.major == 2 and sys.version_info.minor == 7) or sys.version_info.major == 3:
    django = 17
else:
    django = 16    

setup(
    name='YourAppName',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django >=1.6, <1.7' if django == 16 else 'Django >=1.7'],
)
