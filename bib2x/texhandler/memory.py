from __future__ import print_function
# ===================================================================
# bib2x - A BibTex parser and converter.
#
# memory.py - A BibTeX handler keeping the contents in memory
#
# (c) Daniel Krajzewicz 2011-2014, 2022-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
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
class StoringTeXhandler(handler.BibTeXhandler):
    """A BibTeX handler keeping the entries in memory"""
    
    def __init__(self):
        """Constructor
        """
        self._entries = {}
        self._entryIDs = []
        self._stringMap = {}
        self._stringMapKeys = []
    
        self._groupNames = []
        self._groups = {}

    
    def startDocument(self):
        """Called at the begin of a document's processing"""
        pass
    
    
    def addStringDefinition(self, key, value):
        """Adds the definition of a string

        Stores the definition in the self._stringMap dictionary.
        
        Args:
            key (str): The shortcut for the string.
            value (str): The value of the string.
        
        Todo: 
            Remove self._stringMapKeys
        """
        self._stringMap[key] = value
        self._stringMapKeys.append(key)

    
    def addComment(self, key, value):
        """Adds a comment
        
        This implementation is somehow "magic" as it targets
        parsing JabRef comments that contain a group assignment.
        
        Args:
            key (str): The name of the comment?
            value (str): The value of the comment.
        
        Todo: 
            Extract JabRef-parsing.
        """
        if not value.strip().startswith("jabref-meta: groupstree"):
            return
        value = value[value.find("0"):]
        lines = value.split("\n")
        c = ""
        tree = []
        lastLevel = 0
        for l in lines:
            c = c + l.strip()
            i = c.rfind(";")
            #print "%s %s %s %s" % (i, len(c)-1, c[i-2], c[i-2-5:])
            if i==len(c)-1 and len(c)>2 and c[i-1]!='\\':
                d = c[:c.find("\\;")].strip()
                level = int(d[:d.find(" ")])
                name = d[d.find(":")+1:]
                if level<=lastLevel:
                    tree = tree[:-(lastLevel - level + 1)]
                lastLevel = level
                tree.append(name)
        
                if level!=0:
                    d = c[c.find(";")+1:].strip()
                    d = d[d.find(";")+1:d.rfind(";")]
                    items = filter(None, d.split("\;"))
                    gName = "/".join(tree)
                    if gName not in self._groupNames:
                        self._groupNames.append(gName)
                    if gName not in self._groups:
                        self._groups[gName] = []
                    self._groups[gName].extend(items)
                #print "------------\n" + c[:20]
                c = ""
    
    
    def startEntry(self, entryID):
        """Called if a new entry is started to being parsed.

        Begins entry by storing it in internal containers.
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        self._entries[entryID] = {}
        self._entryIDs.append(entryID)


    def addField(self, entryID, key, value):
        """Called if a new attribute of an entry shall be added.
        
        Stores the attribute in the self._entries[entryID] dictionary.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            value (str): The value of the attribute
        """
        self._entries[entryID][key] = value


    def addField2(self, entryID, key, pairs):
        """Called if a new attribute consisting of multiple named fields shall be added.
        
        Allocates a dictionary entry in self._entries[entryID] with the given key.
        Inserts the given pairs as key/values into this dictionary.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            pairs (List[Tuple[str, str]]): The value of the attribute
        """
        if ukey not in self._entries[entryID]:
            self._entries[entryID][key] = {}
        for p in pairs:
            self._entries[entryID][key][p[0]] = p[1]

    
    def closeEntry(self, entryID):
        """Closes the entry
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        pass


    def endDocument(self):
        """Called after parsing a document"""
        pass
        
