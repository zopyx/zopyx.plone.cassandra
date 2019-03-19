from setuptools import setup, find_packages
import os

version = '0.5.0'

setup(name='zopyx.plone.cassandra',
      version=version,
      description="Show all assigned local roles within a subtree for any Plone 5 site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Andreas Jung',
      author_email='info@zopyx.com',
      url='http://pypi.python.org/pypi/zopyx.plone.cassandra',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopyx', 'zopyx.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
