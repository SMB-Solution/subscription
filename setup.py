# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in subscription/__init__.py
from subscription import __version__ as version

setup(
	name='Subscription',
	version=version,
	description='Subscription',
	author='Subscription',
	author_email='Subscription',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)