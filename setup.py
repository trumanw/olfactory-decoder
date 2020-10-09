"""
olfactory-decoder
A library to train/predict smell of molecular compounds and \
    potentially discover new fragrance.
"""
import os
import versioneer
from setuptools import setup

short_description = __doc__.split("\n")

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:])

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_package_data(data_root, package_root):
    files = []
    for root, dirnames, filenames in os.walk(data_root):
        for fn in filenames:
            files.append(os.path.relpath(os.path.join(root, fn), package_root))
    return files

setup(
    name = "olfactorydecoder",
    author = "Chunan Wu",
    author_email = "chunan.woo@gmail.com",
    description = "A library to train/predict smell of molecular compounds",
    license = "MIT",
    keywords = "olfactory, fragrance, scaffold network, active learning",
    url = "https://www.olfactory.ai",
    packages = [
        "olfactorydecoder",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={'console_scripts': []},
    package_data={'olfactorydecoder': find_package_data('olfactorydecoder/data', 'olfactorydecoder')},
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)