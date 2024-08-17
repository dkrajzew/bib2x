from __future__ import print_function
# ===================================================================
# test_bib2x.py
#
# Tests module for bib2x
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/morphoxes
# - http://www.krajzewicz.de/blog/morphoxes.php
#
# Available under the BSD license.
# ===================================================================
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "bib2x"))
import bib2x


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "bib2x").replace("pytest.py", "bib2x").replace("__main__.py", "bib2x")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        bib2x.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """Usage: bib2x [options]

bib2x: error: Input file name is missing, please use the option '--input' / '-i'.
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        bib2x.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """Usage: bib2x [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i INPUT, --input=INPUT
                        The BibTeX file to load
  -o OUTPUT, --output=OUTPUT
                        The file to write
  -f FORMAT, --format=FORMAT
                        The type of file to write ['json']
"""


def test_main_version(capsys):
    """Test behaviour when help is wished"""
    try:
        bib2x.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """bib2x 0.4.0
"""

