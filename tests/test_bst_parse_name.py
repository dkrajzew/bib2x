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
import bib2x.bstparser as bstparser


# --- test classes ------------------------------------------------------------
class TestBSTParser_ParseName(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._parser = bstparser.BSTParser()


    def test__bst_parse_name__no_comma__ttb(self):
        """Tests for parsing a name with no comma, from 'Tame the BeaST'"""
        assert(self._parser.parse_name_no_comma("jean de la fontaine")==["", "jean de la", "fontaine", ""])
        assert(self._parser.parse_name_no_comma("jean de la fontaine")==["", "jean de la", "fontaine", ""])
        assert(self._parser.parse_name_no_comma("Jean de la fontaine")==["Jean", "de la", "fontaine", ""])
        assert(self._parser.parse_name_no_comma("Jean {de} la fontaine")==["Jean de", "la", "fontaine", ""])
        assert(self._parser.parse_name_no_comma("jean {de} {la} fontaine")==["", "jean", "de la fontaine", ""])
        assert(self._parser.parse_name_no_comma("Jean {de} {la} fontaine")==["Jean de la", "", "fontaine", ""])
        assert(self._parser.parse_name_no_comma("Jean De La Fontaine")==["Jean De La", "", "Fontaine", ""])
        assert(self._parser.parse_name_no_comma("jean De la Fontaine")==["", "jean De la", "Fontaine", ""])
        assert(self._parser.parse_name_no_comma("Jean de La Fontaine")==["Jean", "de", "La Fontaine", ""])

    def test__bst_parse_name__one_comma__ttb(self):
        """Tests for parsing a name with one comma, from 'Tame the BeaST'"""
        assert(self._parser.parse_name_one_comma("De la Fontaine, Jean")==["Jean", "De la", "Fontaine", ""])
        assert(self._parser.parse_name_one_comma("de la fontaine, Jean")==["Jean", "de la", "fontaine", ""])
        assert(self._parser.parse_name_one_comma("De La Fontaine, Jean")==["Jean", "", "De La Fontaine", ""])
        assert(self._parser.parse_name_one_comma("de La Fontaine, Jean")==["Jean", "de", "La Fontaine", ""])
        assert(self._parser.parse_name_one_comma("jean de la fontaine,")==["", "jean de la", "fontaine", ""])



