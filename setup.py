# ===================================================================
# bib2x - A BibTex parser and converter.
#
# Setup module
#
# (c) Daniel Krajzewicz 2011-2014, 2022-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# 
# Available under the BSD license.
# ===================================================================



# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bib2x",
    version="0.2.0",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="A BibTex parser and converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://bib2x.readthedocs.org/',
    download_url='http://pypi.python.org/pypi/bib2x',
    project_urls={
        'Documentation': 'https://bib2x.readthedocs.io/',
        'Source': 'https://github.com/dkrajzew/bib2x',
        'Tracker': 'https://github.com/dkrajzew/bib2x/issues',
        'Discussions': 'https://github.com/dkrajzew/bib2x/discussions',
    },
    license='BSD',
    # add modules
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'bib2x = bib2x:main'
        ]
    },
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Artistic Software"
    ],
    python_requires='>=3, <4',
)

