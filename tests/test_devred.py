"""Tests of the devred loader"""

from specloaders.loaders import devred_loader


def test_loading_function():
    """Test that the loading function works."""
    spectrum = devred_loader.devred("tests/data/test_devred_spec.dat")
    assert len(spectrum.spectral_axis) == 1755
    assert len(spectrum.flux) == 1755
    assert spectrum.spectral_axis.unit == "Angstrom"
    assert spectrum.flux.unit == "1e-15 erg / (Angstrom cm2 s)"
    assert spectrum.spectral_axis[0].value == 7215.724
    assert spectrum.spectral_axis[-1].value == 3399.02
    assert spectrum.flux[0].value == 0.28555588853771226
    assert spectrum.flux[-1].value == 1.3884094506483154
