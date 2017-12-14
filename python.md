---
layout: page
title: Python API
navigation: 6
---

# WCxf Python API

The WCxf Python package requires Python version 3.5 or above. It can be installed with the command

```bash
pip3 install wcxf
```
This also installs the [command line interface](cli.html).

## Classes

The `wcxf` package provides three main classes to interact with EFT, basis and Wilson coefficient files, namely `wcxf.EFT`, `wcxf.Basis`, and `wcxf.WC`.
All three classes provide `load` and `dump` methods to read and write them from/to JSON or YAML files. The `WC` class also provides `translate` and `match` methods to translate the numerical values to a different basis or match them to a different EFT.

## API documentation

See the [detailed documentation](/wcxf/) of all functions and methods.
