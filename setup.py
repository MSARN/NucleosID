#! /usr/bin/env python

import os
import re

from setuptools import setup, find_packages

version = re.search(
    '^VERSION\s*=\s*\'(.*)\'',
    open('nucleosid/nucleosid.py').read(),
    re.M
).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open('requirements.txt') as requirements:
    install_requires = requirements.read()

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


setup(
    name='nucleosid',
    version=version,
    description='Identification of RNA post-transcriptional modifications',
    long_description=long_descr,
    install_requires=install_requires,
    author='LSMIS',
    url='https://github.com/MSARN/nucleosid',
    contact='yfrancois@unistra.fr',
    packages=find_packages(include=['nucleosid']),
    entry_points={
        "console_scripts": ['nucleosid = nucleosid.nucleosid:main']
    },
    python_requires='>=3.0',
    keywords=['tkinter'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    include_package_data=True,
    package_data={
        'nucleosid': ['databases/*.csv', 'images/*.png']
                 }
)
