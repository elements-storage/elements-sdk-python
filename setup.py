#!/usr/bin/env python
# coding: utf-8

"""
    ELEMENTS API

    The version of the OpenAPI document: 2
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "elements-sdk"
VERSION = "3.3.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ELEMENTS API",
    author="ELEMENTS Media Storage",
    author_email="info@elements.tv",
    url="https://github.com/elements-storage/elements-sdk-python",
    keywords=["elements", "api"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description="ELEMENTS Python SDK"
)
