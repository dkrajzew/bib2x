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


    # generic parsing
    def test__one_entry1(self):
        content = """@Article{T1, author = "A. Bcd", title = "Title"}"""
        self._parser.parse(content, self._handler)
        assert (list(self._handler._entries.keys())==["T1"])
        assert (self._handler._entries["T1"]=={"author": ["A. Bcd"], "bibtex-type": "Article", "title": "Title"})
        
    def test__one_entry2(self):
        content = """@Article{T1,
author = "A. Bcd", 
title = "Title"}
"""
        self._parser.parse(content, self._handler)
        assert (list(self._handler._entries.keys())==["T1"])
        assert (self._handler._entries["T1"]=={"author": ["A. Bcd"], "bibtex-type": "Article", "title": "Title"})        
        

    def test__two_entries1(self):
        content = """@Article{T1, author = "A. Bcd", title = "Title1"}, @Article{T2, author = "E. Fgh", title = "Title2"}"""
        self._parser.parse(content, self._handler)
        assert (list(self._handler._entries.keys())==["T1", "T2"])
        assert (self._handler._entries["T1"]=={"author": ["A. Bcd"], "bibtex-type": "Article", "title": "Title1"})
        assert (self._handler._entries["T2"]=={"author": ["E. Fgh"], "bibtex-type": "Article", "title": "Title2"})
        
    def test__two_entries2(self):
        content = """@Article{T1,
author = "A. Bcd", 
title = "Title1"}, 

@Article{T2, 
    author = "E. Fgh", 
    title = "Title2"
}
"""
        self._parser.parse(content, self._handler)
        assert (list(self._handler._entries.keys())==["T1", "T2"])
        assert (self._handler._entries["T1"]=={"author": ["A. Bcd"], "bibtex-type": "Article", "title": "Title1"})
        assert (self._handler._entries["T2"]=={"author": ["E. Fgh"], "bibtex-type": "Article", "title": "Title2"})
        



