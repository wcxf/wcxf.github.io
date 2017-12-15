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

## Translation

To translate a Wilson coefficient file to a different basis of the same EFT (e.g. the `flavio` basis), run

```bash
wcxf translate flavio my_wet_jms_coeffs.yml
```

Note that basis names are case sensitive; check the [list of existing bases](bases.html) to find the correct spelling.

## Match

To match Wilson coefficients from a UV to an IR EFT, e.g. from SMEFT to WET,  run

```bash
wcxf match WET JMS my_smeft_warsaw_coeffs.yml
```

Note that EFT and basis names are case sensitive; check the [list of existing EFTs and bases](bases.html) to find the correct spelling.

## Source

The source code can be found [on Github](https://github.com/wcxf/wcxf-python).
