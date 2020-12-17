from io import BytesIO
import logging as logger
from gif import __version__
from wand.image import Image
from .utils import display


def test_version():
    assert __version__ == "0.1.0"


def test_utils_display(png: BytesIO):
    with Image(file=png) as img:
        display(img)