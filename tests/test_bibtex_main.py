#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - Tests bibtex main"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2023-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.4.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import bib2x.bibtex as bibtex


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "bibtex").replace("pytest.py", "bibtex").replace("__main__.py", "bibtex")


# --- test functions ------------------------------------------------
def test_bibtex_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        bibtex.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """usage: bibtex [-h] [--version] input
bibtex: error: the following arguments are required: input
"""


def test_bibtex_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        bibtex.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out.replace("optional arguments", "options")) == """usage: bibtex [-h] [--version] input

A bibtex clone

positional arguments:
  input

options:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

(c) Daniel Krajzewicz 2024-2025
"""
    assert patchName(captured.err) == ""


def test_bibtex_main_version(capsys):
    """Test behaviour when help is wished"""
    try:
        bibtex.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """bibtex 0.4.0
"""
    assert patchName(captured.err) == ""


def test_bibtex_main_minbst(capsys, tmp_path):
    """Test behaviour when help is wished"""
    p1 = tmp_path / "min.bst"
    p1.write_text("""ENTRY {}{}{}
FUNCTION {test}
{"de la Cierva y Codorn{\’\i}u, Juan"
#1 "{ff - }{vv - }{ll}" format.name$ top$}
READ
EXECUTE{test}
""")
    ret = bibtex.main([str(p1)])
    assert ret==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == "Juan - de la Cierva y - Codorn\\’\\iu\n"
    assert patchName(captured.err) == """"""

