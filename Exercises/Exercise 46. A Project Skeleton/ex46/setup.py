try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 46. A Project Skeleton',
	'author': 'Nayef',
	'url': '',
	'download_url': '',
	'author_email': 'nayeffalkhaldi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['bin'],
	'scripts': ['bin\\run.py'],
	'name': 'ex46'
}

setup(**config)