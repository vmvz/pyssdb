from setuptools import setup
import pyssdb
import re
import os
import sys

setup(
    name='ssdb3',
    version=pyssdb.__version__,
    author=re.sub(r'\s+<.*', r'', pyssdb.__author__),
    author_email=re.sub(r'(^.*<)|(>.*$)', r'', pyssdb.__author__),
    url=pyssdb.__url__,
    description=('A SSDB Client Library for Python3.'),
    long_description=open('README.rst').read(),
    license='BSD',
    keywords='ssdb',
    py_modules=['ssdb3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
