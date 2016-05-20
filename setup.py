# coding=utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='zero',
    version='0.1',
    packages=['zero'],
    url='',
    author='Yuhang Xu',
    author_email='xuyuhang2015@163.com',
    classifiers=(),
    description='Python dict utils',
    long_description='Python dict utils',
    test_suite='tests'
)