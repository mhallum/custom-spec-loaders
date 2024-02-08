"""Tests of the larionov loader"""

import pytest
from specutils import Spectrum1D

from specloaders.loaders import larionov_loader

TEST_SPEC_FILENAME = "tests/data/test_larionov_spec.dat"
EXPECTED_PARAMETERS = {
    "wave_first": 7213.71,
    "wave_last": 3201.50,
    "flux_first": 0.501152,
    "flux_last": 1.39872,
    "n_points": 1844,
    "wave_units": "Angstrom",
    "flux_units": "1e-15 erg / (Angstrom cm2 s)",
}


def test_loading_function():
    """Test that the loading function works."""
    spectrum = larionov_loader.larionov("tests/data/test_larionov_spec.dat")
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_first"]
    assert spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[0].value == pytest.approx(EXPECTED_PARAMETERS["flux_first"])
    assert spectrum.flux[-1].value == pytest.approx(EXPECTED_PARAMETERS["flux_last"])


def test_loader():
    """Test with the specutils loader"""
    spectrum = Spectrum1D.read(
        "tests/data/test_larionov_spec.dat",
        format="larionov",
    )
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_first"]
    assert spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[0].value == pytest.approx(EXPECTED_PARAMETERS["flux_first"])
    assert spectrum.flux[-1].value == pytest.approx(EXPECTED_PARAMETERS["flux_last"])


def test_force_increasing():
    """Test that the `force_increasing` parameter works."""
    spectrum = Spectrum1D.read(
        "tests/data/test_larionov_spec.dat",
        format="larionov",
        force_increasing=True,
    )
    assert len(spectrum.spectral_axis) == EXPECTED_PARAMETERS["n_points"]
    assert spectrum.spectral_axis.unit == EXPECTED_PARAMETERS["wave_units"]
    assert spectrum.flux.unit == EXPECTED_PARAMETERS["flux_units"]
    assert spectrum.spectral_axis[-1].value == EXPECTED_PARAMETERS["wave_first"]
    assert spectrum.spectral_axis[0].value == EXPECTED_PARAMETERS["wave_last"]
    assert spectrum.flux[-1].value == pytest.approx(EXPECTED_PARAMETERS["flux_first"])
    assert spectrum.flux[0].value == pytest.approx(EXPECTED_PARAMETERS["flux_last"])
