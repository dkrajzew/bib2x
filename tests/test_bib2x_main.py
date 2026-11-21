#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - Tests bib2x main"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2023-2025, Daniel Krajzewicz"
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
import bib2x.bib2x as bib2x



# --- some presets --------------------------------------------------
turing1 = """@String{j-J-LOND-MATH-SOC       = "Journal of the London Mathematical Society"}
@Article{Turing:1935:ELR,
  author =       "A. M. Turing",
  title =        "Equivalence of left and right almost periodicity",
  journal =      j-J-LOND-MATH-SOC,
  volume =       "10",
  pages =        "284--285",
  year =         "1935",
  CODEN =        "JLMSAK",
  ISSN =         "0024-6107",
  ISSN-L =       "0024-6107",
  bibdate =      "Sat Nov 19 13:23:32 2005",
  bibsource =    "http://www.math.utah.edu/pub/bibnet/authors/t/turing-alan-mathison.bib",
  URL =          "http://turing.ecs.soton.ac.uk/browse.php/B/10",
  acknowledgement = ack-nhfb,
  keywords =     "almost periodic functions; Dirichlet series",
  ZMnumber =     "0012.40404",
}
"""



# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "bib2x").replace("pytest.py", "bib2x").replace("__main__.py", "bib2x")


# --- test functions ------------------------------------------------
def test_bib2x_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        bib2x.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """usage: bib2x [-h] [--version] [-f FORMAT] [--report.keys]
             [--properties.remove PROPERTIES_REMOVE]
             [--properties.keep PROPERTIES_KEEP] [--json.compact]
             [--json.indent JSON_INDENT]
             input output
bib2x: error: the following arguments are required: input, output
"""


def test_bib2x_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        bib2x.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    help_text = HELP_PRE_3_13 if sys.version_info < (3,13) else HELP_POST_3_13
    assert patchName(captured.out.replace("optional arguments", "options")) == help_text


def test_bib2x_main_version(capsys):
    """Test behaviour when the version shall be printed"""
    try:
        bib2x.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """bib2x 0.4.0
"""




def test_bib2x_main_turing2html(capsys, tmp_path):
    """Test behaviour when the version shall be printed"""
    p = tmp_path / "hello1.bib"
    p.write_text(turing1)
    o = tmp_path / "hello1.html"
    ret = bib2x.main(["--format", "html", str(p), str(o)])
    assert ret==0
    captured = capsys.readouterr()
    assert o.read_text() == """<ul>\n<li>[Turing:1935:ELR] A. M. Turing. <b>Equivalence of left and right almost periodicity</b>. <i>Journal of the London Mathematical Society</i>, volume:10, pages::284&ndash;285 1935. <a class="bpURLlink" href="http://turing.ecs.soton.ac.uk/browse.php/B/10"><img border="0" src="images/url.png" alt="more..."/></a> Keywords:  <span class="bpKeyword">almost periodic functions</span> <span class="bpKeyword">Dirichlet series</span></li>\n</ul>\n"""




HELP_PRE_3_13 = """usage: bib2x [-h] [--version] [-f FORMAT] [--report.keys]
             [--properties.remove PROPERTIES_REMOVE]
             [--properties.keep PROPERTIES_KEEP] [--json.compact]
             [--json.indent JSON_INDENT]
             input output

A BibTeX converter with bst support

positional arguments:
  input
  output

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -f FORMAT, --format FORMAT
                        The type of file to write ['json', 'html']
  --report.keys         report keys when parsing
  --properties.remove PROPERTIES_REMOVE
                        remove listed properties
  --properties.keep PROPERTIES_KEEP
                        keep only listed properties
  --json.compact        write each entry into one line
  --json.indent JSON_INDENT
                        the level of indentation to use

(c) Daniel Krajzewicz 2011-2014, 2023-2025
"""

HELP_POST_3_13 = """usage: bib2x [-h] [--version] [-f FORMAT] [--report.keys]
             [--properties.remove PROPERTIES_REMOVE]
             [--properties.keep PROPERTIES_KEEP] [--json.compact]
             [--json.indent JSON_INDENT]
             input output

A BibTeX converter with bst support

positional arguments:
  input
  output

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -f, --format FORMAT   The type of file to write ['json', 'html']
  --report.keys         report keys when parsing
  --properties.remove PROPERTIES_REMOVE
                        remove listed properties
  --properties.keep PROPERTIES_KEEP
                        keep only listed properties
  --json.compact        write each entry into one line
  --json.indent JSON_INDENT
                        the level of indentation to use

(c) Daniel Krajzewicz 2011-2014, 2023-2025
"""