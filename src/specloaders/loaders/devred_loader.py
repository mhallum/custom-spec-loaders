"""Module containing the Specutils Spectrum1D loader for files produced by my devred program."""

import numpy as np
from astropy import units as u
from specutils import Spectrum1D
from specutils.io.registers import data_loader


@data_loader("devred", extensions=["dat"], force=True)
def devred(filename: str, force_increasing: bool = False) -> Spectrum1D:
    """Load a spectrum from a file produced by my devred program.

    This is basicaly a .dat file with two columns. The first column is the
    wavelength in Angstroms and the second column is the flux in units of
    erg/s/cm^2/Angstrom. It is also assumed that the first line of the file
    contains the header.

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

    x, y = np.loadtxt(filename, skiprows=1, delimiter=" ", unpack=True)
    if (x[0] > x[-1]) and force_increasing:
        x = x[::-1]
        y = y[::-1]
    return Spectrum1D(
        spectral_axis=x * u.AA,
        flux=y / 10**-15 * u.ferg / u.s / u.cm / u.cm / u.AA,
    )
