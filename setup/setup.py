import sys
import os
import subprocess

# Check if Python 3.8 is installed
if sys.version_info < (3, 8):
    print("Python 3.8 or later is required.")
    sys.exit(1)
# Install the required packages
os.system("pip3 install -r packagerequirement.txt")