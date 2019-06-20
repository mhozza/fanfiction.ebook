#!/usr/bin/env python
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


setup(
    name="ff_ebook",
    version="0.2.0",
    url="https://github.com/mhozza/fanfiction.ebook",

    author="Neia Neutuladh, Michal Hozza",
    author_email="dhasenan@gmail.com, mhozza@gmail.com",

    description="Ebook generator for fanfiction sites.",

    packages=find_packages(exclude=('tests', 'examples',)),

    install_requires=['beautifulsoup4', 'requests', 'lxml'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
