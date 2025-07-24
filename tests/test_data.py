"""Data test."""
import os
import glob
import unittest
from pathlib import Path

from linkml_runtime.loaders import yaml_loader, json_loader
from vega_scverse.spec_models.specification import ViewConfiguration

DATA_DIR = Path(__file__).parent / "data" / "examples" / "valid"

EXAMPLE_FILES = DATA_DIR.glob('*.json')


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            obj = json_loader.load(path, target_class=ViewConfiguration)
            assert obj
