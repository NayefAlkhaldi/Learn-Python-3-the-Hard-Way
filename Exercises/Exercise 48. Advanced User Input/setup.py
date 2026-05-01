try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 48. Advanced User Input',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['pytest'],
	'packages': ['lexicon'],
	'scripts': [''],
	'name': 'ex48'
}

setup(**config)