# bib2x

[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/bib2x.svg)](https://pypi.python.org/pypi/bib2x)
![test](https://github.com/dkrajzew/bib2x/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/bib2x)](https://pepy.tech/project/bib2x)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/bib2x/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/bib2x?branch=main)
[![Documentation Status](https://readthedocs.org/projects/bib2x/badge/?version=latest)](https://bib2x.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


Introduction
============

__bib2x__ is a tool for parsing and processing BibTeX files.

__bib2x__ is currently under development. The latest version is 0.4.0.

The current use cases are:

* Convert BibTeX-files to JSON


Examples
--------

```console
bib2x -i turing.bib -o turing.json -f json
```

Converts the BibTeX-file "turing.bib" into the JSON-file "turing.json" with the BibTeX entries.

```console
bib2x -i turing.bib -o turing.html -f html
```

Converts the BibTeX-file "turing.bib" into a file named "turing.html" that contains a HTML list with the BibTeX entries.


Background
----------

Being a somehow busy scientific coworker *and* a software guy, I wanted to render [my publications](https://www.krajzewicz.de/daniel/publications.php) for [my web site](https://www.krajzewicz.de).

For this purpose, I wrote [BibPres](https://www.krajzewicz.de/bibpres/index.php), a commercial tool that uses JSON to store a publications list and JavaScript to render and interact with it.

__bib2x__ is a rework of BibPres released as open source. Currently, only the parser is being ported as I want to change it so that it renders plain HTML, not a JSON file.

If you have any comments, ideas, or critics, please let me know.


License
-------

__bib2x__ is licensed under the [BSD license](license.md).


Documentation
=============

Running on the Command Line
===========================

__bib2x__ is implemented in [Python](https://www.python.org/). It is started on the command line.

__bib2x__ reads the BibTeX file defined using the **--input *&lt;BIBTEX_FILE&gt;*** option. It converts it to the format defined using the option **--format *&lt;FORMAT&gt;*** and saves it under the name defined using the option **--output *&lt;FILE&gt;***. Currently, only "*json*" is available as destination format.


Examples
--------

```console
bib2x -i turing.bib -o turing.json
```

Converts the BibTeX-file "turing.bib" into the JSON-file "turing.json".


Command line arguments
----------------------

The script can be started on the command line with the following options:

* **--input *&lt;BIBTEX_FILE&gt;*** / **-i *&lt;BIBTEX_FILE&gt;***: The BibTeX file to load
* **--output *&lt;FILE&gt;*** / **-o *&lt;FILE&gt;***: The file to write
* **--format *&lt;FORMAT&gt;*** / **-f *&lt;FORMAT&gt;***: The type of file to write ['json']
* **--help**: Show a help message
* **--version**: Show the version information


Further Links
=============

* A complete documentation is located at:
    * <https://bib2x.readthedocs.io/en/latest/> and
    * <https://krajzewicz.de/docs/bib2x/index.html>
* Discussions are open at <https://github.com/dkrajzew/bib2x/discussions>
* The github repository is located at: <https://github.com/dkrajzew/bib2x>
* The issue tracker is located at: <https://github.com/dkrajzew/bib2x/issues>
* The PyPI page is located at: <https://pypi.org/project/bib2x/>


ChangeLog for bib2x
===================

bib2x-0.4.0 (27.03.2023)
------------------------

* Work on the documentation
* Added HTML output
* Further tests


bib2x-0.2.0 (08.03.2023)
------------------------

* Initial version





