import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    return "1.9.7-58-g02454c8"


setup(
    name="AegeanTools",
    version=get_version(),
    author="Paul Hancock",
    author_email="Mr.Paul.Hancock@gmail.com",
    description="The Aegean source finding program, and associated tools.",
    # license = "BSD",
    # keywords="example documentation tutorial",
    url="https://github.com/PaulHancock/Aegean",
    long_description=read('README.md'),
    packages=['AegeanTools'],
    install_requires=['numpy>=1.10',
                      'scipy>=0.16',
                      'astropy>=1.0',
                      'lmfit>=0.9.2',
                      'pprocess>=0.5'],
    scripts=['scripts/aegean', 'scripts/BANE', 'scripts/SR6', 'scripts/AeRes', 'scripts/MIMAS']
)