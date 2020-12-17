from ctypes import util
from io import BytesIO
import gif
import pytest


def test_too_large_square():
    target_length = 10
    width, height = (20, 20)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (target_length, target_length)


def test_too_small_square():
    target_length = 10
    width, height = (5, 5)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (target_length, target_length)


def test_already_perfect_square():
    target_length = 10
    width, height = (target_length, target_length)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (target_length, target_length)


def test_too_wide():
    target_length = 10
    width, height = (20, 4)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (10, 2)


def test_too_thin():
    target_length = 10
    width, height = (5, 4)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (10, 8)


def test_too_tall():
    target_length = 10
    width, height = (10, 20)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (5, 10)


def test_too_short():
    target_length = 10
    width, height = (4, 5)
    w, h = gif.Image.fit_dimensions(width, height, target_length)
    assert (w, h) == (8, 10)


@pytest.mark.visual
def test_resize(png: BytesIO):
    with gif.Image(file=png) as img:
        img.display()
        img.resize_to_bound(10)
        img.display()