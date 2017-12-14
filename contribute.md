---
layout: page
title: Contributing
navigation: 4
---

# Contributing to WCxf

Since WCxf is an extensible format, users can contribute to extending it in various ways.

## Adding a new EFT

A new EFT can be defined by writing an EFT file containing the name (and an optional description) as well as the name of the *sectors* defined in the EFT (see the paper for an explanation of sectors). For instance, a YAML file could look like

```yaml
eft: My EFT
description: My description
sectors:
  sector1:
  sector2:
```

Submitting this file to the [official EFT & basis repository](http://github.com/wcxf/wcxf-bases) via a pull request automatically makes the EFT available to the Python command line tool at the next release.


## Adding a new basis

Adding a new basis is similar to adding a new EFT; a basis definition file has to be written and can be submitted to the [EFT & basis repository](http://github.com/wcxf/wcxf-bases) via a pull request.

Before submission, it is useful to validate the format of the file by running

```bash
wcxf validate basis my_basis.yml
```
