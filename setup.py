from setuptools import setup


setup(name='ZH-tools',
      version='0.1.0',
      description='Chinese related scripts',
      url='https://github.com/julienbaley/zhtools',
      packages=['zhtools'],
      package_dir={'': 'lib'},
      tests_require=['nose>=1.3.4'],
      test_suite='nose.collector',
      )
