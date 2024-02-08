"""Loader for the files produced by an IDL program written by Valeri M. Larionov."""


# pylint: disable=duplicate-code

from typing import Tuple

import numpy as np
from astropy import units as u
from specutils import Spectrum1D
from specutils.io.registers import data_loader


def _parse_line_lariononv(line: str) -> Tuple[float, float]:
    line = line.strip()  # remove leading and trailing whitespace
    if " " in line:  # x, y values separated by space
        x, y = line.split()
    else:  # x, y one word because y is negative (- instead of space)
        x, abs_y = line.split("-", 1)
        y = f"-{abs_y}"
    return float(x), float(y)


def _read_larionov_xy(
    filename: str,
) -> Tuple[np.ndarray, np.ndarray]:
    x_list = []
    y_list = []
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        new_x, new_y = _parse_line_lariononv(line)
        x_list.append(new_x)
        y_list.append(new_y)
    return np.array(x_list), np.array(y_list)


@data_loader("larionov", extensions=["dat"], force=True)
def larionov(file_name: str, force_increasing: bool=False) -> Spectrum1D:
    """Load a spectrum from a file produced by an IDL program written by Valeri M. Larionov.

    This is basicaly a .dat file with two columns. The first column is the
    wavelength in Angstroms and the second column is the flux in units of
    erg/s/cm^2/Angstrom.

    Parameters
    ----------
    file_name : str
        The name of the file containing the spectrum.

    force_increasing : bool, optional
        If True, the spectrum will be flipped so that the spectral axis is
        increasing. This is useful for spectra that are stored in decreasing
        order. By default, this is False.

    Returns
    -------
    Spectrum1D
        The loaded spectrum. Note that the flux is converted to units of
        10^-15 erg/s/cm^2/Angstrom
    """
    x, y = _read_larionov_xy(file_name)
    if (x[0] > x[-1]) and force_increasing:
        x = x[::-1]
        y = y[::-1]
    return Spectrum1D(
        spectral_axis=x * u.AA,
        flux=y / 10**-15 * u.ferg / u.s / u.cm / u.cm / u.AA,  # type: ignore
    )
