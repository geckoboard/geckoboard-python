from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name='geckoboard',
  version='0.2.4',
  description='The official Python client for the Geckoboard Datasets API',
  long_description=readme(),
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