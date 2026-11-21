#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""handler.py - BibTeXhandler definition (abstract class)"""
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- class definitions -----------------------------------------------------
class BibTeXhandler:
    """The base class for handlers for processing BibTeX"""

    def __init__(self, indent, compact):
        """Constructor

        Does nothing.
        """
        self._indent = indent
        self._compact = compact


    def startDocument(self):
        """Called at the begin of a document's processing"""
        pass # pragma: no cover


    def addStringDefinition(self, key, value):
        """Adds the definition of a string

        Args:
            key (str): The shortcut for the string.
            value (str): The value of the string.
        """
        pass # pragma: no cover


    def addComment(self, key, value):
        """Adds a comment

        Args:
            key (str): The name of the comment?
            value (str): The value of the comment

        todo: Check semantics
        """
        pass # pragma: no cover


    def startEntry(self, entryID):
        """Called if a new entry is started to being parsed.

        Args:
            entryID (str): The ID (key) of the entry
        """
        pass # pragma: no cover


    def addField(self, entryID, key, value):
        """Called if a new attribute of an entry shall be added.

        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            value (str): The value of the attribute
        """
        pass # pragma: no cover


    def addField2(self, entryID, key, pairs):
        """Called if a new attribute consisting of multiple named fields shall be added.

        This is only used when parsing JabRef file-fields.

        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            pairs (List[Tuple[str, str]]): The value of the attribute
        """
        pass # pragma: no cover


    def closeEntry(self, entryID):
        """Closes the entry

        Args:
            entryID (str): The ID (key) of the entry
        """
        pass # pragma: no cover


    def endDocument(self):
        """Called after parsing a document"""
        pass # pragma: no cover



    def _ind(self, num):
        return ' '*(self._indent * num)
