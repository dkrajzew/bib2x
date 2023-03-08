from __future__ import print_function
# ===================================================================
# bib2x - A BibTex parser and converter.
#
# A JSON exporting BibTeX handler
#
# (c) Daniel Krajzewicz 2011-2014, 2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
# 
# Available under the BSD license.
# ===================================================================


# --- imports -------------------------------------------------------
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import re
import sqlite3
try: from . import handler
except: import handler


# --- classes -------------------------------------------------------
class JSONexportingTeXhandler(handler.BibTeXhandler):
    """A BibTex handler that exports entries as JSON."""

    def __init__(self, fdo):
        """Constructor
        """
        self._entry = ""
        self._firstEntry = True
        self._fdo = fdo
        self._hadOne = False


    def startDocument(self):
        """Called at the begin of a document's processing"""
        self._fdo.write("var bib={\n \"entries\":{\n")
        pass
    
    
    def addStringDefinition(self, key, value):
        """Adds the definition of a string
        
        This implementation does nothing.
        
        Args:
            key (str): The shortcut for the string.
            value (str): The value of the string.
        
        Todo: 
            check whether string definition should not be saved
        """
        pass
        
    
    def addComment(self, key, value):
        """Adds a comment
        
        This implementation does nothing.
        
        Args:
            key (str): The name of the comment?
            value (str): The value of the comment.
        """
        pass

    
    def startEntry(self, entryID):
        """Called if a new entry is started to being parsed.

        Begins entry encoding by generating a named JSON map.
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        self._hadOne = False
        self._entry = ""
        self._entry = self._entry + '  "%s":{\n' % entryID


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
            self._entry = self._entry + ",\n"
        if isinstance(value, int):
            self._entry = self._entry + '   "%s":%s' % (key, value)
        elif isinstance(value, list):
            self._entry = self._entry + '   "%s":%s' % (key, value)
        else:
            self._entry = self._entry + '   "%s":"%s"' % (key, value)
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
            self._entry = self._entry + ",\n"
        self._entry = self._entry + '   "%s":{' % (key)
        r = []
        for p in pairs:
            r.append('"%s":"%s"' % (p[0], p[1]))
        self._entry = self._entry + ",".join(r)
        self._entry = self._entry + '}'
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
        self._entry = self._entry + "\n  }" 
        self._fdo.write(self._entry) 


    def endDocument(self):
        """Called after parsing a document"""
        self._fdo.write("\n }\n};\n")
        
