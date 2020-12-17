from io import BytesIO
import logging as logger
import gif
from wand.image import Image


def test_version():
    assert gif.__version__ == "0.1.0"


def test_display(png: BytesIO):
    with Image(file=png) as img:
        gif.display(img)
