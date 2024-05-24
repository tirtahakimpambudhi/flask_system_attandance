#!/bin/bash

# Update package list and install CMake
apt-get update && apt-get install -y cmake

# Install Python dependencies
pip3.12 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt
