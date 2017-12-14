---
layout: page
title: Command line
navigation: 5
---

# WCxf command line interface

The WCxf command line tool requires Python version 3.5 or above. It can be installed with the command

```bash
pip3 install wcxf
```

It can be used for conversion, validation, translation, and matching of WCxf files. You can display all options by running

```bash
wcxf -h
```

in the terminal.

## Conversion

To convert a WCxf file in YAML format to JSON, run

```bash
wcxf convert json my_file.yml
```

## Validation

To validate a basis file, run

```bash
wcxf validate basis my_basis.yml
```

and for a Wilson coefficient file

```bash
wcxf validate wc my_coeffs.yml
```

It accepts input files in YAML or JSON format.
