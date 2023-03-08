from __future__ import print_function
# ===================================================================
# bib2x - A BibTex parser and converter.
#
# BibTeXhandler module initialisation
#
# (c) Daniel Krajzewicz 2011-2014, 2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
# 
# Available under the BSD license.
# ===================================================================


# --- classes -------------------------------------------------------
class BibTeXhandler:
    """The base class for handlers for processing BibTeX"""

    def __init__(self):
        """Constructor
        
        Does nothing.
        """
        pass
    
    
    def startDocument(self):
        """Called at the begin of a document's processing"""
        pass
    
    
    def addStringDefinition(self, key, value):
        """Adds the definition of a string
        
        Args:
            key (str): The shortcut for the string.
            value (str): The value of the string.
        """
        pass
        
    
    def addComment(self, key, value):
        """Adds a comment
        
        Args:
            key (str): The name of the comment?
            value (str): The value of the comment
        
        todo: Check semantics
        """
        pass

    
    def startEntry(self, entryID):
        """Called if a new entry is started to being parsed.
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        pass


    def addField(self, entryID, key, value):
        """Called if a new attribute of an entry shall be added.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            value (str): The value of the attribute
        """
        pass


    def addField2(self, entryID, key, pairs):
        """Called if a new attribute consisting of multiple named fields shall be added.
        
        This is only used when parsing JabRef file-fields.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            pairs (List[Tuple[str, str]]): The value of the attribute
        """
        pass


    def closeEntry(self, entryID):
        """Closes the entry
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        pass


    def endDocument(self):
        """Called after parsing a document"""
        pass
        