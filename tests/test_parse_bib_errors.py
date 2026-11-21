#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - Tests bib2x main"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
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
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import bib2x.texfile as texfile
import bib2x.texhandler.memory as memoryhandler


# --- test classes ------------------------------------------------------------
class TestBSTParser_ParseName(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._parser = texfile.TeXfile()
        self._handler = memoryhandler.StoringTeXhandler()


    def test__broken_entry1(self):
        content = """@Article{T1, author = "A. Bcd", title ="""
        try:
            self._parser.parse(content, self._handler)
            assert False # pragma: no cover
        except ValueError as e:
            assert type(e)==type(ValueError())
            assert str(e)=="closing bracket is missing"


