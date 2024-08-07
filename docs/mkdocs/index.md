[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/bib2x.svg)](https://pypi.python.org/pypi/bib2x)
[![Downloads](https://pepy.tech/badge/bib2x)](https://pepy.tech/project/bib2x)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/bib2x/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/bib2x?branch=main)
[![Documentation Status](https://readthedocs.org/projects/bib2x/badge/?version=latest)](https://bib2x.readthedocs.io/en/latest/?badge=latest)


[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


Introduction
------------

__bib2x__ is a tool for parsing and processing BibTeX files.

__bib2x__ is currently under development. The latest version is 0.4.0.

The current use cases are:

* Convert BibTeX-files to JSON;
* Convert BibTeX-files to a HTML list.

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

