from PIL import Image
from io import BytesIO


def test_display(png: BytesIO):
    im = Image.open(png)
    im.show()