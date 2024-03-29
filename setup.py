#!/usr/bin/env python3

import os
import subprocess

from setuptools import setup, find_packages

TARGET_DEV = os.getenv("TARGET_DEV")

install_requires = []
with open("requirements.txt", "r", encoding="utf-8") as requirements:
    install_requires=requirements.read().splitlines()

if TARGET_DEV is None:
    try:
        last_commit = subprocess.check_output("git rev-parse --verify --short HEAD", shell=True).strip().decode()
        commit_of_last_tag = subprocess.check_output("git rev-list --tags --max-count=1 --abbrev-commit", shell=True).strip().decode()
        tags = subprocess.check_output("git rev-list --tags --max-count=1", shell=True).strip().decode()
        last_tag = subprocess.check_output("git describe --tags --abbrev=0", shell=True).strip().decode()

        if last_commit == commit_of_last_tag:
            _version = last_tag
        else:
            _version = f"0.0.0+{last_commit}"
    except:
        print("Error: Version could not be generated")
        _version = "0.0.0"
        raise
else:
    _version = "0.0.0"

setup(
    name="rpi-season-screen",
    version=_version,
    description="RPI Sense Hat Display",
    install_requires=install_requires,
    packages=find_packages(exclude=["test", "test.*"]),
    entry_points={"console_scripts": ["rpi-season-screen = rpi_season_screen.bin.daemon:main"]},
)
