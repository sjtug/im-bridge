#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="imbridge",
    version="0.1",
    url='https://github.com/sjtug/im-bridge',
    author='SJTUG',
    author_email='sjtug+subscribe@googlegroups.com',
    description='Bridge the gap between IM platforms',
    install_requires=[
        "zenlog",
        "requests"
    ],
    packages=find_packages(),
    license="GPL3+",
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: "
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
    ],
    entry_points={
        'console_scripts': [
            'im-bridge = cli.cli:main',
        ],
    },
    keywords="im bridge",
)
