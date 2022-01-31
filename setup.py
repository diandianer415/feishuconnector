#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from feishuconnector import _version


setup(
    name='feishuconnector',
    version=_version,
    description=(
        'connect feishu content franchise'
    ),
    long_description=open('README.rst').read(),
    author='Changhao Jiang',
    author_email='jch@puyuan.tech',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'requests >= 2.22.0'
    ],
)