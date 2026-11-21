#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - a bibtex clone"""
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import sys
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bib2x.bstparser as bstparser


# --- functions -------------------------------------------------------------
# --- main
def main(arguments=None):
    # build options
    parser = argparse.ArgumentParser(prog='bibtex',
        description='A bibtex clone',
        epilog='(c) Daniel Krajzewicz 2024-2025')
    parser.add_argument("input")
    parser.add_argument('--version', action='version', version='%(prog)s 0.4.0')
    args = parser.parse_args(arguments)
    parser = bstparser.BSTParser()
    parser.process_file(args.input)
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover
