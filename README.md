# Custom Spec Loaders

A collection of custom [specutils](https://specutils.readthedocs.io/en/stable/) loaders.

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/mhallum/custom-spec-loaders/actions/workflows/ci.yml/badge.svg)](https://github.com/mhallum/custom-spec-loaders/actions/workflows/ci.yml)

## Installation

The easiest way to install the loaders is to simply download the `.py` files containing the loaders to the `~.specutils` folder. (See section on [Available Loaders](#available-loaders) for list of available loaders with their file names.)

## Usage

Once the loaders are installed in the `~.specutils` directory, the normal [specutils](https://specutils.readthedocs.io/en/stable/) reader can be used to load a spectrum.

Example:

```python
from specutils import Spectrum1D

spectrum = Spectrum1D.read("filename.dat", format="devred")
```

The [devred](#devred) and [larionov](#larionov) loaders have the additional parameter `force_increasing`, which is False by default. If set to true, the spectrum will be flipped (if necessary) so that the spectral axis is increasing. This is useful for spectra that are stored in decreasing order.

Example:

```python
from specutils import Spectrum1D

spectrum = Spectrum1D.read("filename.dat", format="devred", force_increasing=True)
```

## Available Loaders

All loader files are located in the `./src/specloaders` folder.

| name | Description | file |
| ------| -----| ---- |
| [devred](#devred) | Load a spectrum from a file produced by my devred program. | `devred_loader.py` |
| [larionov](#larionov) | Load a spectrum from a file produced by an IDL program written by Valeri M. Larionov. | `larionov_loader.py` |

### devred

Use this loader to load a spectrum form a file produced by my devred program.

This is basicaly a `.dat` file with two columns. The first column is the
wavelength in Angstroms and the second column is the flux in units of
$\rm{erg}~\rm{s}^{-1}~\rm{cm}^{-2}~\AA^{-1}$. Note that the flux is converted to units of $10^{-15}~\rm{erg}~\rm{s}^{-1}~\rm{cm}^{-2}~\AA^{-1}$ when loaded.

> [!WARNING]
> This loader assumes that the first line of the file is the header. If your file does not contain a header, the first line of the file will be ignored.

### larionov

Use this loader Load a spectrum from a file produced by an IDL program written by Valeri M. Larionov.

This is basicaly a `.dat` file with two columns. The first column is the
wavelength in Angstroms and the second column is the flux in units of $\rm{erg}~\rm{s}^{-1}~\rm{cm}^{-2}~\AA^{-1}$. Note that the flux is converted to units of $10^{-15}~\rm{erg}~\rm{s}^{-1}~\rm{cm}^{-2}~\AA^{-1}$ when loaded.
