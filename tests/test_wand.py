from io import BytesIO
from wand.image import Image
from wand.display import display


def test_display(png: BytesIO):
    im = Image(file=png)
    display(im), ":1"