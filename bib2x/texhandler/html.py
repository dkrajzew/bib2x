#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""A BibTex handler that exports entries as HTML
"""
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


# --- format definitions ----------------------------------------------------
formats = {
    "periodical":       "<b>%title%</b>, ?month:%month% ?%year%.",
    "article":          "%authorREP%. <b>%title%</b>. <i>%journal%</i>?, volume:%volume%??, number:(%number%)??, pages::%pages%??, month:%month%? %year%.",
    "book":             "%authorREP%. <b>%title%</b>?volume:, volume %volume%??series: of %series%?. %publisher%?address:, %address%??edition:, %edition% edition?, ?month:%month% ?%year%.",
    "booklet":          "%authorREP%. <b>%title%</b>. ?howpublished:%howpublished%, ??address: %address%, ??month:%month% ?%year%.",
    "conference":       "%authorREP%. <b>%title%</b>. In: ?editor:%editorREP%, editor, ?<i>%booktitle%</i>?volume:, volume %volume%??series: of %series%??pages:, pages %pages%??address:, %address%?, ?month:%month% ?%year%. ?organization:%organization%, ??publisher:%publisher%?.",
    "electronic":       "%authorREP%. <b>%title%</b>. ?howpublished:%howpublished%, ??month:%month% ?%year%.",
    "inbook":           "%authorREP%. <b>%title%</b>?volume:, volume %volume%??series: of %series%??type:, %type%??chapter: %chapter%??pages:, %pages%??publisher:, %publisher%??address:, %address%??edition:, %edition% edition?, ?month:%month% ?%year%.",
    "incollection":     "%authorREP%. <b>%title%</b>. In: ?editor:%editorREP%, editor, ?<i>%booktitle%</i>?volume:, volume %volume%??series: of %series%??type:, %type%??chapter: %chapter%??pages:, %pages%?.?publisher: %publisher%??address:, %address%??edition:, %edition% edition?, ?month:%month% ?%year%.",
    "inproceedings":    "%authorREP%. <b>%title%</b>. In: ?editor:%editorREP%, editor, ?<i>%booktitle%</i>?volume:, volume %volume%??series: of %series%??pages:, %pages%??address:, %address%?, ?month:%month% ?%year%. ?organization:%organization%, ??publisher:%publisher%.?",
    "manual":           "%authorREP%. <b>%title%</b>. ?organization:%organization%??address:, %address%??edition:, %edition% edition?, ?month:%month% ?%year%.",
    "mastersthesis":    "%authorREP%. <b>%title%</b>. ?type:%type%, ?%school%?address:, %address%?, ?month:%month% ?%year%.",
    "misc":             "%authorREP%. <b>%title%</b>. ?howpublished:%howpublished%, ??month:%month% ?%year%.",
    "patent":           "%authorREP%. <b>%title%</b>. %year%.",
    "phdthesis":        "%authorREP%. <b>%title%</b>. ?type:%type%, ?%school%?address:, %address%?, ?month:%month% ?%year%.",
    "proceedings":      "%editorREP%, editor. <b>%title%</b>?volume:, volume %volume%??series: of %series%??pages:, %pages%??address:, %address%?, ?month:%month% ?%year%. ?organization:%organization%, ??publisher:%publisher%?.",
    "standard":         "%authorREP%. <b>%title%</b>. ?howpublished:%howpublished%, ??month:%month% ?%year%.",
    "techreport":       "%authorREP%. <b>%title%</b>. ?type:%type%??number: %number%??type:, ??institution:%institution%, ??address:%address%, ??month:%month% ?%year%.",
    "unpublished":      "%authorREP%. <b>%title%</b>. ?month:%month% ?%year%."
}


# --- class definitions -----------------------------------------------------
class HTMLexportingTeXhandler:
    """A BibTex handler that exports entries as HTML."""

    def __init__(self, fdo):
        """Constructor
        
        Args:
            fdo (file descriptor): The file to write to
        """
        self._fdo = fdo
        self._stringMap = {}
        self._currentBibTeXKey = None
        self._currentAttrs = {}
    
    
    def startDocument(self):
        """Called at the begin of a document's processing"""
        self._itemIndex = 0
        self._fdo.write("<ul>\n")
    
    
    def addStringDefinition(self, key, value):
        """Adds the definition of a string
        
        Args:
            key (str): The shortcut for the string.
            value (str): The value of the string.
        """
        self._stringMap[key] = value
        
    
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
        self._currentBibTeXKey = entryID
        self._currentAttrs = {}


    def addField(self, entryID, key, value):
        """Called if a new attribute of an entry shall be added.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            value (str): The value of the attribute
        """
        self._currentAttrs[key] = value


    def addField2(self, entryID, key, pairs):
        """Called if a new attribute consisting of multiple named fields shall be added.
        
        This is only used when parsing JabRef file-fields.
        
        Args:
            entryID (str): The ID (key) of the entry
            key (str): The name of the attribute
            pairs (List[Tuple[str, str]]): The value of the attribute
        """
        self._currentAttrs[key] = pairs


    def fillTemplate(self, tpl, fields):
        """Parses the template and fills it with the given values
        
        Args:
            tpl (str): The entry-type specific template to fill
            fields (dict): The dictionary of the entry's attributes
        
        Returns:
            The template filled with the given values
        """
        ret = ""
        tmp = ""
        isOpt = False
        hadAll = False
        i = 0
        while i<len(tpl):
            if tpl[i]=='?':
                if isOpt:
                    isOpt = False
                    if hadAll:
                        ret += tmp
                else:
                    isOpt = True
                    hadAll = True
                    tmp = ""
            elif tpl[i]=='%':
                b = i + 1
                e = b
                while tpl[e]!="%" and e<len(tpl):
                    e += 1
                k = tpl[b:e]
                if k not in fields:
                    hadAll = False
                    if not isOpt:
                        print ("Missing required attribute '%s' in %s" % (k, self._currentBibTeXKey))
                elif isOpt:
                    tmp += str(fields[k])
                else:
                    ret += str(fields[k])
                i = e
            elif isOpt:
                tmp += tpl[i]
            else:
                ret += tpl[i]
            i += 1
        return ret


    def closeEntry(self, entryID):
        """Closes the entry
        
        Args:
            entryID (str): The ID (key) of the entry
        """
        bibtexType = "article" if "bibtex-type" not in self._currentAttrs else self._currentAttrs["bibtex-type"].lower()
        self._currentAttrs["authorREP"] = ", ".join(self._currentAttrs["author"]) if "author" in self._currentAttrs else ""
        self._currentAttrs["editorREP"] = ", ".join(self._currentAttrs["editor"]) if "editor" in self._currentAttrs else ""
        self._currentAttrs["short"] = entryID
        
        # bibtex key
        ret = "[" + self._currentAttrs["short"] + "] "
        # render bibtex
        tpl = formats[bibtexType]
        ret += self.fillTemplate(tpl, self._currentAttrs)
        # files
        if "file" in self._currentAttrs:
            name = self._currentAttrs["file"]["name"]
            extension = os.path.splitext(name)
            url = self._currentAttrs["file"]["url"]
            ret += ' <a class="bpFilelink" href="' + url + '">'
            ret += '<img border="0" src="images/' + extension + '.png" alt="' + name + '"/>';
            ret += "</a>";
        # URL
        if "url" in self._currentAttrs:
            ret += ' <a class="bpURLlink" href="' + self._currentAttrs["url"] + '"><img border="0" src="images/url.png" alt="more..."/></a>'
        # DOI
        if "doi" in self._currentAttrs:
            ret += ' <a class="bpDOIlink" href="' + self._currentAttrs["doi"] + '"><img border="0" src="images/doi.png" alt="more..."/></a>'
        # abstract
        abstractShowOption = "trigger" # default: trigger, "trigger", "show", "off"
        if "abstract" in self._currentAttrs:
            if abstractShowOption=="default" or abstractShowOption=="trigger":
                ret += ' <a class="bpAbstractT" href="" onclick="javascript:return showAbstract(' + str(self._itemIndex) + ');">Show Abstract</a><div  style="display: none;" id="abstract' + str(self._itemIndex) + '"'
            elif abstractShowOption=="show":
                ret += '<div'
            if abstractShowOption=="default" or abstractShowOption=="trigger" or abstractShowOption=="show":
                ret += ' class="bpAbstract">' + self._currentAttrs["abstract"] + '</div>';
        # keywords
        keywordsShowOption = "show" # default: show, "show", "off"
        if "keywords" in self._currentAttrs:
            listview_keywordsPre = " Keywords: "
            listview_keywordsPost = ""
            listview_keywordsHead = ' <span class="bpKeyword">'
            listview_keywordsTail = '</span>'
            ret += listview_keywordsPre
            for k in self._currentAttrs["keywords"]:
                ret += listview_keywordsHead + k + listview_keywordsTail
            ret += listview_keywordsPost    
        # write
        self._fdo.write("<li>" + ret + "</li>\n")
        # 
        self._itemIndex += 1


    def endDocument(self):
        """Called after parsing a document"""
        self._fdo.write("</ul>\n")
        