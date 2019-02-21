"""Setup for pysmarty package."""

import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="pysmarty",
    version="0.1",
    author="Theo Nicolau",
    author_email="theo.nicolau@gmail.com",
    description="Python API for Salda Smarty Modbus TCP",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/z0mbieprocess/pysmarty",
    packages=setuptools.find_packages(),
    install_requires=list(val.strip() for val in open('requirements.txt')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
