try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 49. Making Sentences',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex49'],
	'scripts': [''],
	'name': 'ex49'
}

setup(**config)