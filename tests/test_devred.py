"""Tests for the devred loader"""

# pylint: disable=duplicate-code

from specutils import Spectrum1D

from specloaders import devred_loader

TEST_SPEC_FILENAME = "tests/data/test_devred_spec.dat"
EXPECTED_PARAMETERS = {
    "wave_first": 7215.724,
    "wave_last": 3399.02,
    "flux_first": 0.28555588853771226,
    "flux_last": 1.3884094506483154,
    "n_points": 1755,
    "wave_units": "Angstrom",
    "flux_units": "1e-15 erg / (Angstrom cm2 s)",
}


def test_loading_function():
    """Test that the loading function works."""
    spectrum = devred_loader.devred(TEST_SPEC_FILENAME)
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_first"]
    assert spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[0].value == EXPECTED_PARAMETERS["flux_first"]
    assert spectrum.flux[-1].value == EXPECTED_PARAMETERS["flux_last"]


def test_loader():
    """Test with the specutils loader"""
    spectrum = Spectrum1D.read(
        "tests/data/test_devred_spec.dat",
        format="devred",
    )
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_first"]
    assert spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[0].value == EXPECTED_PARAMETERS["flux_first"]
    assert spectrum.flux[-1].value == EXPECTED_PARAMETERS["flux_last"]


def test_force_increasing():
    """Test that the `force_increasing` option works."""
    spectrum = Spectrum1D.read(
        "tests/data/test_devred_spec.dat",
        format="devred",
        force_increasing=True,
    )
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert (
        spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_first"]
    )
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[-1].value == EXPECTED_PARAMETERS["flux_first"]
    assert spectrum.flux[0].value == EXPECTED_PARAMETERS["flux_last"]
