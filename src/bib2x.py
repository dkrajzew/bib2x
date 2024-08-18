#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""bib2x - A BibTex parser and converter.
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


# --- imports ---------------------------------------------------------------
import sys, os
import argparse
import texfile
import texhandler.handler
import texhandler.json
import texhandler.html


# --- functions -------------------------------------------------------------
# --- main
def main(arguments=None):
    """Main method
    
    The application reads the file defined by --input / -i _&lt;BIBTEX_FILE&gt;_ and saves the contents
    to the file defined using the option --output / -o _&lt;FILE&gt;_, converting them to the 
    format defined using the option --format / -f _&lt;FORMAT&gt;_.
    
    Args:
        arguments (List[str]): The command line arguments, parsed as options using OptionParser.


    Options
    -------
    
    The following options must be set:

    --input / -i _&lt;BIBTEX_FILE&gt;_:
        The BibTeX file to load
    
    --output / -o _&lt;FILE&gt;_:
        The file to write
    
    The following options are optional:
    
    --format / -f _&lt;FORMAT&gt;_:
        The type of file to write ['json']
    """
    # build options
    parser = argparse.ArgumentParser(prog='bib2x', 
        description='A BibTeX converter with bst support', 
        epilog='(c) Daniel Krajzewicz 2011-2014, 2020-2024')
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument('--version', action='version', version='%(prog)s 0.4.0')
    parser.add_argument("-f", "--format", default="json", help="The type of file to write ['json']")
    args = parser.parse_args(arguments)
    # check options
    if args.format!="json" and args.format!="html":
        print("bib2x: error: Unknown output format; only 'json' and 'html' are supported.", file=sys.stderr)
        return 2
    # process
    texF = texfile.TeXfile()
    content = texF.read2string(args.input)
    fdo = open(args.output, "w")
    handler = None
    if args.format=="json":
        handler = texhandler.json.JSONexportingTeXhandler(fdo)
    elif args.format=="html":
        handler = texhandler.html.HTMLexportingTeXhandler(fdo)
    texF.parse(content, handler)
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover
