#!/usr/bin/env python
import os

from setuptools import setup


ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

requirements = [
    'six >= 1.4.0',
]

version = None
exec(open('dockerpycreds/version.py').read())

with open('./test-requirements.txt') as test_reqs_txt:
    test_requirements = [line for line in test_reqs_txt]


setup(
    name="docker-pycreds",
    version=version,
    description="Python bindings for the docker credentials store API",
    url='https://github.com/shin-/dockerpy-creds',
    license='Apache License 2.0',
    packages=[
        'dockerpycreds',
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)
