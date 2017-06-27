from setuptools import setup

setup(
  name='geckoboard',
  version='1.0.0',
  description='A Python client for the Geckokboard Datasets API',
  url='https://github.com/geckoboard/geckoboard-python',
  author='Dan Bahrami',
  author_email='dan@geckoboard.com',
  license='MIT',
  keywords='geckoboard datasets',
  packages=['geckoboard'],
  install_requires=['requests'],
  tests_require=['nose', 'mock'],
)