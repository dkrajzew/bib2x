Running on the Command Line
===========================

__bib2x__ is implemented in [Python](https://www.python.org/). It is started on the command line.

__bib2x__ reads the BibTeX file defined using the **--input *&lt;BIBTEX_FILE&gt;*** option. It converts it to the format defined using the option **--format *&lt;FORMAT&gt;*** and saves it under the name defined using the option **--output *&lt;FILE&gt;***. Currently, only "*json*" is available as destination format.


Examples
--------

```console
bib2x -i turing.bib -o turing.json -f json
```

Converts the BibTeX-file "turing.bib" into the JSON-file "turing.json" with the BibTeX entries.

```console
bib2x -i turing.bib -o turing.html -f html
```

Converts the BibTeX-file "turing.bib" into a file named "turing.html" that contains a HTML list with the BibTeX entries.


Command line arguments
----------------------

The script can be started on the command line with the following options:

* **--input *&lt;BIBTEX_FILE&gt;*** / **-i *&lt;BIBTEX_FILE&gt;***: The BibTeX file to load
* **--output *&lt;FILE&gt;*** / **-o *&lt;FILE&gt;***: The file to write
* **--format *&lt;FORMAT&gt;*** / **-f *&lt;FORMAT&gt;***: The type of file to write ['json']
* **--help**: Show a help message
* **--version**: Show the version information

