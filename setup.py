from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Products.s3storage',
      version=version,
      description="s3storage for plone",
      long_description="""\
s3storage for plone is an eggified version of the former s3storage""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='s3 plone zodb',
      author='Christoph Scheid',
      author_email='c@shriNOSPAM.de',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'boto',
          'python-memcached'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
