from setuptools import setup

setup(
  name='geckoboard',
  version='0.2.1',
  description='The official Python client for the Geckoboard Datasets API',
  url='https://github.com/geckoboard/geckoboard-python',
  author='Geckoboard',
  author_email='dan@geckoboard.com',
  license='MIT',
  keywords=['geckoboard', 'datasets', 'api', 'python'],
  packages=['geckoboard'],
  install_requires=['requests'],
  tests_require=['nose', 'mock'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ]
)