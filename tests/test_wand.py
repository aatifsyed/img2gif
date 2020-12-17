from io import BytesIO
import gif


def test_resize(png: BytesIO):
    im = gif.Image(file=png)
    w, h = im.size
    im.display()
    im.resize(w // 2, h // 2)
    im.display()
    im.rotate