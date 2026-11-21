#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - Tests for bib2x json output"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2011-2014, 2023-2025, Daniel Krajzewicz"
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
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import util
from util import text_read as tread
from util import copy_files as copy
import bib2x.bib2x as bib2x


# --- helper functions ----------------------------------------------
def pame(string, path="<DIR>"):
    return util.pname(string, "bib2x", path)



# --- test functions ------------------------------------------------
# -- plain --
def test_main_turingpart2json_plain(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main([str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
    "Turing:1935:ELR":{
        "bibtex-type":"Article",
        "author":['A. M. Turing'],
        "title":"Equivalence of left and right almost periodicity",
        "journal":"Journal of the London Mathematical Society",
        "volume":"10",
        "pages":"284&ndash;285",
        "year":1935,
        "coden":"JLMSAK",
        "issn":"0024-6107",
        "issn-l":"0024-6107",
        "bibdate":"Sat Nov 19 13:23:32 2005",
        "bibsource":"http://www.math.utah.edu/pub/bibnet/authors/t/turing-alan-mathison.bib",
        "url":"http://turing.ecs.soton.ac.uk/browse.php/B/10",
        "acknowledgement":"Nelson H. F. Beebe, University of Utah, Department of Mathematics, 110 LCB, 155 S 1400 E RM 233, Salt Lake City, UT 84112-0090, USA, Tel: +1 801 581 5254, FAX: +1 801 581 4148, e-mail: beebe@math.utah.edu, beebe@acm.org, beebe@computer.org (Internet), URL: http://www.math.utah.edu/~beebe/",
        "keywords":['almost periodic functions', 'Dirichlet series'],
        "zmnumber":"0012.40404"
    }
]"""


# -- indent --
def test_main_turingpart2json_indent2(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main(["--json.indent", "2", str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
  "Turing:1935:ELR":{
    "bibtex-type":"Article",
    "author":['A. M. Turing'],
    "title":"Equivalence of left and right almost periodicity",
    "journal":"Journal of the London Mathematical Society",
    "volume":"10",
    "pages":"284&ndash;285",
    "year":1935,
    "coden":"JLMSAK",
    "issn":"0024-6107",
    "issn-l":"0024-6107",
    "bibdate":"Sat Nov 19 13:23:32 2005",
    "bibsource":"http://www.math.utah.edu/pub/bibnet/authors/t/turing-alan-mathison.bib",
    "url":"http://turing.ecs.soton.ac.uk/browse.php/B/10",
    "acknowledgement":"Nelson H. F. Beebe, University of Utah, Department of Mathematics, 110 LCB, 155 S 1400 E RM 233, Salt Lake City, UT 84112-0090, USA, Tel: +1 801 581 5254, FAX: +1 801 581 4148, e-mail: beebe@math.utah.edu, beebe@acm.org, beebe@computer.org (Internet), URL: http://www.math.utah.edu/~beebe/",
    "keywords":['almost periodic functions', 'Dirichlet series'],
    "zmnumber":"0012.40404"
  }
]"""


def test_main_turingpart2json_indent0(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main(["--json.indent", "0", str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
"Turing:1935:ELR":{
"bibtex-type":"Article",
"author":['A. M. Turing'],
"title":"Equivalence of left and right almost periodicity",
"journal":"Journal of the London Mathematical Society",
"volume":"10",
"pages":"284&ndash;285",
"year":1935,
"coden":"JLMSAK",
"issn":"0024-6107",
"issn-l":"0024-6107",
"bibdate":"Sat Nov 19 13:23:32 2005",
"bibsource":"http://www.math.utah.edu/pub/bibnet/authors/t/turing-alan-mathison.bib",
"url":"http://turing.ecs.soton.ac.uk/browse.php/B/10",
"acknowledgement":"Nelson H. F. Beebe, University of Utah, Department of Mathematics, 110 LCB, 155 S 1400 E RM 233, Salt Lake City, UT 84112-0090, USA, Tel: +1 801 581 5254, FAX: +1 801 581 4148, e-mail: beebe@math.utah.edu, beebe@acm.org, beebe@computer.org (Internet), URL: http://www.math.utah.edu/~beebe/",
"keywords":['almost periodic functions', 'Dirichlet series'],
"zmnumber":"0012.40404"
}
]"""


# -- indent --
def test_main_turingpart2json_compact(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main(["--json.compact", str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
    "Turing:1935:ELR":{ "bibtex-type":"Article", "author":['A. M. Turing'], "title":"Equivalence of left and right almost periodicity", "journal":"Journal of the London Mathematical Society", "volume":"10", "pages":"284&ndash;285", "year":1935, "coden":"JLMSAK", "issn":"0024-6107", "issn-l":"0024-6107", "bibdate":"Sat Nov 19 13:23:32 2005", "bibsource":"http://www.math.utah.edu/pub/bibnet/authors/t/turing-alan-mathison.bib", "url":"http://turing.ecs.soton.ac.uk/browse.php/B/10", "acknowledgement":"Nelson H. F. Beebe, University of Utah, Department of Mathematics, 110 LCB, 155 S 1400 E RM 233, Salt Lake City, UT 84112-0090, USA, Tel: +1 801 581 5254, FAX: +1 801 581 4148, e-mail: beebe@math.utah.edu, beebe@acm.org, beebe@computer.org (Internet), URL: http://www.math.utah.edu/~beebe/", "keywords":['almost periodic functions', 'Dirichlet series'], "zmnumber":"0012.40404" }
]"""


# -- remove properties --
def test_main_turingpart2json_remove_properties(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main(["--properties.remove", "bibsource,acknowledgement,coden", str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
    "Turing:1935:ELR":{
        "bibtex-type":"Article",
        "author":['A. M. Turing'],
        "title":"Equivalence of left and right almost periodicity",
        "journal":"Journal of the London Mathematical Society",
        "volume":"10",
        "pages":"284&ndash;285",
        "year":1935,
        "issn":"0024-6107",
        "issn-l":"0024-6107",
        "bibdate":"Sat Nov 19 13:23:32 2005",
        "url":"http://turing.ecs.soton.ac.uk/browse.php/B/10",
        "keywords":['almost periodic functions', 'Dirichlet series'],
        "zmnumber":"0012.40404"
    }
]"""


# -- keep properties --
def test_main_turingpart2json_keep_properties(capsys, tmp_path):
    """ """
    copy(tmp_path, ["turing_part.bib"])
    ret = bib2x.main(["--properties.keep", "bibtex-type,author,title", str(tmp_path / "turing_part.bib"), str(tmp_path / "turing_part.json")])
    assert ret==0
    captured = capsys.readouterr()
    assert pame(captured.err) == ""
    assert pame(captured.out) == ""
    assert tread(tmp_path / "turing_part.json") == """"entries":[
    "Turing:1935:ELR":{
        "bibtex-type":"Article",
        "author":['A. M. Turing'],
        "title":"Equivalence of left and right almost periodicity"
    }
]"""
