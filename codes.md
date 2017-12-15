---
layout: page
title: Implementations
navigation: 4
---

# Codes implementing WCxf

This an alphabetical list of open source tools with an importer or exporter for Wilson coefficients in WCxf format. If you have a code to add to this list, [edit this page on Github](https://github.com/wcxf/wcxf.github.io/blob/master/codes.md).

## Overview

Code | Import  | Export |
-----|---------|--------
[DsixTools](#dsixtools) | ✓ | ✓ |
[EOS](#eos) | ✓ |
[flavio](#flavio) | ✓ |
[FlavorKit](#flavorkit) |  | ✓  
[FormFlavor](#formflavor) | ✓ | ✓  
[python-smeftrunner](#python-smeftrunner) | ✓ | ✓ |
[SMEFT Feynman Rules](#smeft-feynman-rules) | ✓ | ✓ |
[SMEFTsim](#smeftsim) | ✓<sup>1</sup> |
[SPheno](#spheno) |  | ✓  
[wcxf-python](#wcxf-python) | ✓ | ✓ |

<sup>1</sup> under development

## DsixTools

[DsixTools](https://dsixtools.github.io/) is a Mathematica package for RG running in the SMEFT, tree-level matching of the SMEFT onto the WET, and RG running in the WET.

Wilson coefficients in the `Warsaw` basis can be translated to and from the DsixTools file format using the functions `WCXFtoSLHA` and `SLHAtoWCXF`. See the [DsixTools manual](https://dsixtools.github.io/files/manual.pdf) for details.

## EOS

[EOS](https://eos.github.io/) is a C++ package for flavour physics phenomenology in the SM and beyond.

An EOS parameter file to set the values of Wilson coefficients can be generated from a WCxf using the command-line utility `wcxf2eos` shipped with the [WCxf CLI](cli.html).

See the [EOS manual](https://eos.github.io/manual/manual.pdf) for detailed usage notes.

## flavio

[flavio](https://flav-io.github.io/) is a Python package for flavour physics phenomenology in the SM and beyond.

Wilson coefficients can be read from a file or directly from a `wcxf.WC` instance (using the [WCxf Python API](python.html))
using the `set_initial_wcxf` method of a `flavio.WilsonCoefficients` instance.
See the [flavio API docs](https://flav-io.github.io/apidoc/flavio/physics/eft.m.html) for details.

## FlavorKit

[FlavorKit](https://arxiv.org/abs/1405.1434) is an extension of the Mathematica package [SARAH](https://sarah.hepforge.org/) that computes 1-loop WET Wilson coefficients for a large class of models.

Numerical values of Wilson coefficients will be exported to WCxf files
if the flag `79` in the Les Houches input file is set to `1`.

## FormFlavor

[FormFlavor](https://formflavor.hepforge.org/) is a Mathematica based tool for computing a broad list of flavor and CP observables in general new physics models.

WCxf files can be imported and exported using the functions `WriteWilsonToJSON` and `ReadWilsonFromJSON`.

## python-smeftrunner

[python-smeftrunner](https://github.com/DsixTools/python-smeftrunner) is a Python package implementing approximately the same functionality as the SMEFTrunner module of [DsixTools](https://dsixtools.github.io/), i.e. RG evolution in the SMEFT.

Wilson coefficients can be imported and exported to and from files or from `wcxf.WC` instances using the [WCxf Python API](python.html).

## SMEFT Feynman Rules

[SMEFT Feynman Rules](http://www.fuw.edu.pl/smeft/) is a Mathematica package evaluating the
Feynman rules for the SMEFT in terms of the physical
(mass-eigenstates) fields of the theory. It works using the
[FeynRules](http://feynrules.irmp.ucl.ac.be/) package.

Wilson coefficient values can be imported and exported using the `WCXFtoSMEFT` and `SMEFTtoWCXF` functions.

## SMEFTsim

[SMEFTsim](https://arxiv.org/abs/1709.06492) is an implementation of the SMEFT in [FeynRules](http://feynrules.irmp.ucl.ac.be/).

A future version of the wcxf-python package will contain the command-line script `wcxf2smeftsim` that will allow to convert a WCxf file to a `param_card.dat` file that can be used to run numerical simulations in MadGraph5_aMC@NLO.

## SPheno

[SPheno](https://spheno.hepforge.org/) is a tool for the phenomenology of supersymmetric models.

Numerical values of Wilson coefficients will be exported to WCxf files
if the flag `79` in the Les Houches input file is set to `1`.

## wcxf-python

See [Python API](python.html)
