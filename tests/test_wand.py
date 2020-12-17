from io import BytesIO
from wand.image import Image
import gif


def test_resize(png: BytesIO):
    im = Image(file=png)
    w, h = im.size
    gif.display(im, title="before")
    im.resize(w // 2, h // 2)
    gif.display(im, title="after")