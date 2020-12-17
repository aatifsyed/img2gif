from typing import Optional
from PIL import Image as pil
import wand.image as wand
from io import BytesIO


def display(image: wand.Image, title: Optional[str] = None):
    """Use Pillow to display an image, since wand's `display` function doesn't always work"""
    with BytesIO() as fp:
        image.save(file=fp)
        pillow: pil.Image = pil.open(fp)
        pillow.show(title=title)