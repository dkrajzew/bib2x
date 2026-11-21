#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - A BibTex parser and converter.

bib2x reads the BibTeX file defined as the first parameter (options may come before).
It converts it to the format defined using the option **--format *&lt;FORMAT&gt;***
and saves it under the name supported as the second parameter.
Currently, only "*json*" and "*html*" are available as destination format.

Options
-------

The following options are optional:

- --format / -f _&lt;FORMAT&gt;_: The type of file to write ['json']

The following arguments must be given:

- input: The BibTeX file to load
- output: The file to write
"""
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import argparse
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import bib2x.texfile as texfile
import bib2x.texhandler.json as jsonhandler
import bib2x.texhandler.html as htmlhandler


# --- functions -------------------------------------------------------------
# --- main
def main(arguments=None):
    """Main method

    Args:
        arguments (List[str]): The command line arguments, parsed as options using OptionParser.
    """
    # build options
    parser = argparse.ArgumentParser(prog='bib2x',
        description='A BibTeX converter with bst support',
        epilog='(c) Daniel Krajzewicz 2011-2014, 2023-2025')
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument('--version', action='version', version='%(prog)s 0.4.0')
    #parser.add_argument('-b', '--bst', help="Defines a bst file to use")
    parser.add_argument("-f", "--format", default="json", help="The type of file to write ['json', 'html']") # !!! use argparse sets
    parser.add_argument("--report.keys", dest="report_keys", action="store_true", help="report keys when parsing")
    parser.add_argument("--properties.remove", dest="properties_remove", default=None, help="remove listed properties")
    parser.add_argument("--properties.keep", dest="properties_keep", default=None, help="keep only listed properties")
    parser.add_argument("--json.compact", dest="json_compact", action="store_true", help="write each entry into one line")
    parser.add_argument("--json.indent", dest="json_indent", type=int, default=4, help="the level of indentation to use")
    args = parser.parse_args(arguments)
    # check options
    if args.format!="json" and args.format!="html":
        print(f"bib2x: error: Unknown output format '{args.format}'; only 'json' and 'html' are supported.", file=sys.stderr)
        return 2
    # process
    tex_file = texfile.TeXfile(args.properties_remove, args.properties_keep)
    fdo = open(args.output, "w", encoding="utf-8") # !!! where closed?
    handler = None
    if args.format=="json":
        handler = jsonhandler.JSONexportingTeXhandler(fdo, args.json_indent, args.json_compact)
    elif args.format=="html":
        handler = htmlhandler.HTMLexportingTeXhandler(fdo)
    content = tex_file.read2string(args.input)
    tex_file.parse(content, handler, args.report_keys)
    return 0


# -- main check
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:])) # pragma: no cover
