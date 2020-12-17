import pytest
import logging as logger
from gif import __version__
from wand.image import Image


def test_version():
    assert __version__ == "0.1.0"
