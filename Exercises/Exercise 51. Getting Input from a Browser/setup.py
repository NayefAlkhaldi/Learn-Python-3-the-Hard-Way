try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 51. Getting Input from Browser',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': [''],
	'scripts': [''],
	'name': 'ex50'
}

setup(**config)