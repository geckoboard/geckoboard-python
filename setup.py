from setuptools import setup


def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()


setup(
    name='geckoboard.py',
    version='0.2.7',
    description='Official Python client for the Geckoboard Datasets API',
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
