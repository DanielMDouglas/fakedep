#!/usr/bin/env python

import setuptools

VER = "0.0.1"

reqs = ["numpy",
        "h5py",
        "argparse",
        ]

setuptools.setup(
    name="fakedep",
    version=VER,
    author="Daniel D. and others",
    author_email="dougl215@slac.stanford.edu",
    description="A package for generating fake edep-sim segments",
    url="https://github.com/DanielMDouglas/fakedep",
    packages=setuptools.find_packages(),
    install_requires=reqs,
    scripts=["bin/fakedep"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    python_requires='>=3.2',
)
