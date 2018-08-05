"""Tests for `papis_tk` package."""

import pytest
from pkg_resources import parse_version

import papis_tk


def test_valid_version():
    """Check that the package defines a valid __version__"""
    assert parse_version(papis_tk.__version__) >= parse_version("0.1.0")
