#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""Tests for bib2x HTML output"""
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
import texhandler.html


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
    opath = os.path.join(d.as_path(), "turing.html")
    bib2x.main(["-f", "html", ipath, opath])
    captured = capsys.readouterr()
    assert patchName(captured.err) == ""
    assert patchName(captured.out) == """Missing required attribute 'booktitle' in Turing:1949:CLR
Missing required attribute 'booktitle' in Turing:1951:LPM
Missing required attribute 'booktitle' in Turing:1953:DCA
Missing required attribute 'booktitle' in Turing:1965:SLB
Missing required attribute 'booktitle' in Randell:1972:ATOb
Missing required attribute 'booktitle' in Cordy:1983:TAN
Missing required attribute 'booktitle' in Cordy:1983:TNG
Missing required attribute 'booktitle' in Good:1992:IRA
Missing required attribute 'booktitle' in Turing:2005:NM
Missing required attribute 'booktitle' in Turing:2005:PEC
Missing required attribute 'booktitle' in Turing:2005:TWL
"""
    assert bread(os.path.join(d.as_path(), "turing.html")) == bread(os.path.join(test_dir, "turing.html"))
    d.cleanup()
    
    
