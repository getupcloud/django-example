#!/usr/bin/env python

from setuptools import setup
import sys

install_requires = []
if sys.version_info.major == 3:
    install_requires.append('mysql-connector-python')

setup(
    name='YourAppName',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=install_requires,
)
