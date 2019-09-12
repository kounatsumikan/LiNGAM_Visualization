# coding: utf-8

from setuptools import setup, find_packages
from pathlib import Path

NAME = 'LiNGAM_Visualization'
VERSION = '0.5.0'

setup(
    name=NAME,
    version=VERSION,
    install_requires=["graphviz", "sklearn", "numpy", "munkres"],
)
