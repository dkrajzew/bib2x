from __future__ import print_function
# ===================================================================
# bib2x - A BibTex parser and converter.
#
# bib2x.py - Main module
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
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from optparse import OptionParser
try: import texfile
except: from . import texfile
try: import texhandler
except: from . import texhandler
try:
    import texhandler
    import texhandler.json
except:
    pass

# --- functions -----------------------------------------------------
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
    optParser = OptionParser(usage="bib2x [options]", version="bib2x 0.2.0")
    optParser.add_option("-i", "--input", dest="input", default=None, help="The BibTeX file to load")
    optParser.add_option("-o", "--output", dest="output", default=None, help="The file to write")
    optParser.add_option("-f", "--format", dest="format", default="json", help="The type of file to write ['json']")
    options, remaining_args = optParser.parse_args(args=arguments)
    # check options
    if options.input is None:
        optParser.error("Input file name is missing, please use the option '--input' / '-i'.")
    if options.output is None:
        optParser.error("Output file name is missing, please use the option '--output' / '-o'.")
    # process
    texF = texfile.TeXfile()
    content = texF.read2string(options.input)
    fdo = open(options.output, "w")
    handler = texhandler.json.JSONexportingTeXhandler(fdo)
    texF.parse(content, handler)
    


# -- main check
if __name__ == '__main__':
    main(sys.argv[1:]) # pragma: no cover
