try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 47. Automated Testing',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [''],
	'name': 'ex47'
}

setup(**config)