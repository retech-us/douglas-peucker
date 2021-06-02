#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="douglas-peucker",
    version="0.1.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
    ],
    packages=["douglas_peucker"],
    install_requires=[],
    rust_extensions=[RustExtension("douglas_peucker.douglas_peucker")],
    include_package_data=True,
    zip_safe=False,
)
