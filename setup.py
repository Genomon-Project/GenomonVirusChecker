#!/usr/bin/env python

from distutils.core import setup

setup(name='genomon_virus_checker',
      version='0.1.0',
      description='Python tools for checking viral sequences',
      author='Yuichi Shiraishi',
      author_email='friend1ws@gamil.com',
      url='https://github.com/Genomon-Project/GenomonVirusChecker.git',
      package_dir = {'': 'lib'},
      packages=['genomon_virus_checker'],
      scripts=['genomon_virus_checker'],
      license='GPL-3'
     )

