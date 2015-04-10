from setuptools import setup, find_packages

"""
import sys

if sys.version_info < (3, 3):
    sys.stderr.write('Serpentine needs >=Python3.3, preferably 3.4\n')
    sys.exit(-1)
"""

setup(name='ZH-tools',
      version='0.1.0',
      description='Chinese related scripts',
      url='https://github.com/julienbaley/zhtools',
      packages=['zhtools',],
      package_dir = {'': 'lib'},
      tests_require = ['nose>=1.3.4'],
      test_suite = 'nose.collector',
     )
