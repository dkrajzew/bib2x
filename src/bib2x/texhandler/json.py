#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A BibTex handler that exports entries as JSON"""
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import sys
import re
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bib2x.texhandler.handler as handler


# --- class definitions -----------------------------------------------------
class JSONexportingTeXhandler(handler.BibTeXhandler):
    """A BibTex handler that exports entries as JSON."""

    def __init__(self, fdo, indent, compact):
        """Constructor

        Args:
            fdo (file descriptor): The file to write to
        """
        handler.BibTeXhandler.__init__(self, indent, compact)
        self._fdo = fdo
        self._entry = ""
        self._firstEntry = True
        self._hadOne = False


    def startDocument(self):
        """Called at the begin of a document's processing"""
        self._fdo.write("\"entries\":[\n")


    def addStringDefinition(self, key, value):
        """Adds the definition of a string

        This implementation does nothing.

        Args:
            key (str): The shortcut for the string
            value (str): The value of the string

        Todo:
            check whether string definition should not be saved
        """
        pass


    def addComment(self, key, value):
        """Adds a comment

        This implementation does nothing.

        Args:
            key (str): The name of the comment?
            value (str): The value of the comment
        """
        pass


    def startEntry(self, entryID):
        """Called if a new entry is started to being parsed.

        Begins entry encoding by generating a named JSON map.

        Args:
            entryID (str): The ID (key) of the entry
        """
        self._hadOne = False
        self._entry = self._ind(1) + '"' + entryID + '":{'
        self._entry += ' ' if self._compact else '\n'


    def addField(self, entryID, key, value):
        """Called if a new attribute of an entry shall be added.

        Appends the attribute encoded as JSON to the current item's
        definition.

        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            value (str): The value of the attribute
        """
        if self._hadOne:
            self._entry += ', ' if self._compact else ',\n'
        ind = "" if self._compact else self._ind(2)
        if isinstance(value, int):
            self._entry += '%s"%s":%s' % (ind, key, value)
        elif isinstance(value, list):
            self._entry += '%s"%s":%s' % (ind, key, value)
        else:
            self._entry += '%s"%s":"%s"' % (ind, key, value)
        self._hadOne = True


    def addField2(self, entryID, key, pairs):
        """Called if a new attribute consisting of multiple named fields shall be added.

        Opens a new attribute with the given name and appends
        the pairs as key/value JSON objects inside it.

        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            pairs (List[Tuple[str, str]]): The value of the attribute
        """
        if self._hadOne:
            self._entry += ","
            if not self._compact:
                self._entry += '\n'
        ind = "" if self._compact else self._ind(2)
        self._entry += '%s"%s":{' % (ind, key)
        r = []
        for p in pairs:
            r.append('"%s":"%s"' % (p[0], p[1]))
        self._entry += ",".join(r)
        self._entry += '}'
        self._hadOne = True


    def closeEntry(self, entryID):
        """Closes the entry

        Args:
            entryID (str): The ID (key) of the entry
        """
        if not self._firstEntry:
            self._entry = ",\n" + self._entry
        else:
            self._firstEntry = False
        self._entry += " }" if self._compact else ("\n" + self._ind(1) + "}")
        self._fdo.write(self._entry)


    def endDocument(self):
        """Called after parsing a document"""
        self._fdo.write("\n]")
