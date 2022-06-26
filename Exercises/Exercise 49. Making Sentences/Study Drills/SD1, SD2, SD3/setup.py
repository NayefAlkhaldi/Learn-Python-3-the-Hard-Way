try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 49. Making Sentences - Study Drills',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Study Drills'],
	'scripts': [''],
	'name': 'ex49-sd'
}

setup(**config)