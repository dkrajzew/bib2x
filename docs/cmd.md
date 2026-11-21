# Running on the Command Line

## Synopsis

```shell
bib2x [-h] [--format FORMAT] [--version]
	  input output
```

## Description

__bib2x__ is implemented in [Python](https://www.python.org/). It is started on the command line.

__bib2x__ reads the BibTeX file defined as the first parameter (options may come before). It converts it to the format defined using the option **--format *&lt;FORMAT&gt;*** option and saves it under the name supported as the second parameter. Currently, only "*json*" and "*html*" are available as destination format.


## Examples

```console
bib2x -f json turing.bib turing.json 
```

Converts the BibTeX-file "turing.bib" into the JSON-file "turing.json" with the BibTeX entries.

```console
bib2x -f html turing.bib turing.html 
```

Converts the BibTeX-file "turing.bib" into a file named "turing.html" that contains a HTML list with the BibTeX entries.


## Command line arguments

The script can be started on the command line with the following options:

* **--format *&lt;FORMAT&gt;*** / **-f *&lt;FORMAT&gt;***: The type of file to write ['json']
* **--help**: Show a help message
* **--version**: Show the version information

It requires two parameters:

* **input**: The bibtex file to read
* **output**: The file to write

