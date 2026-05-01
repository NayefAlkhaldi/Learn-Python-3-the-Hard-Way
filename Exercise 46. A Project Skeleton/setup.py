#!/usr/bin/env python
try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 46. A Project Skeleton',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['pytest', 'setuptools'],
	'packages': find_packages(),
	'scripts': ['bin/sd4.py'],
	'name': 'ex46',
}

setup(**config)