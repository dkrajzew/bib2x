#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""Tests for bib2x json output"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2011-2014, 2020-2024, Daniel Krajzewicz"
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
import shutil
from testfixtures import TempDirectory
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import bib2x
import texhandler
import texhandler.json


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "bib2x").replace("pytest.py", "bib2x").replace("__main__.py", "bib2x")

def bread(path):
    with open(path, "rb") as fd:
        return fd.read()



# --- test functions ------------------------------------------------
def test_main_turing2json(capsys):
    """Test behaviour when help is wished"""
    dir = os.path.split(__file__)[:-1]
    test_dir = os.path.join(*dir)
    d = TempDirectory()
    ipath = os.path.join(d.as_path(), "turing.bib")
    shutil.copy(os.path.join(test_dir, "turing.bib"), ipath)
    opath = os.path.join(d.as_path(), "turing.json")
    bib2x.main([ipath, opath])
    captured = capsys.readouterr()
    assert patchName(captured.err) == ""
    assert patchName(captured.out) == ""
    assert bread(os.path.join(d.as_path(), "turing.json")) == bread(os.path.join(test_dir, "turing.json"))
    d.cleanup()
    
