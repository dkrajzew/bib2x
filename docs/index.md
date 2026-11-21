[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/bib2x/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/bib2x.svg)](https://pypi.org/project/bib2x/)
![test](https://github.com/dkrajzew/bib2x/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/bib2x)](https://pepy.tech/projects/bib2x)
[![Downloads](https://static.pepy.tech/badge/bib2x/week)](https://pepy.tech/projects/bib2x)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/bib2x/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/bib2x?branch=main)
[![Documentation Status](https://readthedocs.org/projects/bib2x/badge/?version=latest)](https://bib2x.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)

#

__bib2x__ - a BibTeX to X converter

## Introduction

__bib2x__ is a command line application for parsing BibTeX files and converting them to other formats, mainly to HTML for showing a bibliography on a web site. __bib2x__ is written in [Python](https://www.python.org/).

The current use cases are:

* convert BibTeX-files to JSON;
* convert BibTeX-files to HTML.

__bib2x__ converts LaTeX-characters into utf8 characters, utf8 entities, or HTML entities. <!-- When exporting to text or HTML, __bib2x__ can apply a .bst (BibTeX style) file for proper rendering. As such, __bib2x__ is capable to format names. -->

__bib2x__ is currently under development. The latest version is 0.4.0.


## Usage

```console
bib2x -f json turing.bib turing.json 
```

Converts the BibTeX-file "turing.bib" into the JSON-file "turing.json" with the BibTeX entries.

```console
bib2x -f html turing.bib turing.html 
```

Converts the BibTeX-file "turing.bib" into a file named "turing.html" that contains a HTML list with the BibTeX entries.


## Documentation

The documentation consists of a [man-page like call documentation](cmd.md).

If you want to contribute, you may check the [API documentation](api_bib2x.md) or visit [bib2x on github](https://github.com/dkrajzew/bib2x) where besides the code you may find the [bib2x issue tracker](https://github.com/dkrajzew/bib2x/issues) or a [discussions about bib2x](https://github.com/dkrajzew/bib2x/discussions) section.

Additional documentation includes a page with relevant [links](links.md or, the [ChangeLog](changes.md). You may find the complete documentation at the [bib2x readthedocs pages](https://bib2x.readthedocs.io/).

## Installation

The current version is 0.4.0. You may install the latest release using pip:

```console
python -m pip install bib2x
```

Or download the [latest release](https://github.com/dkrajzew/bib2x/releases/tag/0.4.0) from github. You may as well clone or download the [bib2x git repository](https://github.com/dkrajzew/bib2x). There is also a page about [installing bib2x](install.md) which lists further options.


## License

__bib2x__ is licensed under the [BSD license](license.md).


## Background

Being a somehow busy scientific coworker *and* a software guy, I wanted to render [my publications](https://www.krajzewicz.de/daniel/publications.php) for [my web site](https://www.krajzewicz.de).

For this purpose, I wrote [BibPres](https://www.krajzewicz.de/bibpres/index.php), a commercial tool that uses JSON to store a publications list and JavaScript to render and interact with it.

__bib2x__ is a rework of BibPres released as open source. Currently, only the parser is being ported as I want to change it so that it renders plain HTML, not a JSON file.

If you have any comments, ideas, or critics, please let me know.


## Status &amp; Contributing

__bib2x__ is in an early development stage. Yet, it is not my major project, so extensions and new versions may take some time. If you need something or have a comment, you may drop me a mail or [add an issue](https://github.com/dkrajzew/bib2x/issues).

