from io import BytesIO
from typing import Optional, Tuple

import wand.image as wand
from PIL import Image as pil


class Image(wand.Image):
    def resize_to_bound(self, bound: int):
        """Resize such that the longest edge is `bound`

        Args:
            length (int): [description]
        """
        w, h = self.fit_dimensions(self.width, self.height, bound)
        self.resize(w, h)

    @classmethod
    def fit_dimensions(cls, width, height, bound) -> Tuple[float, float]:
        """classmethod for testability"""
        largest = max(width, height)
        factor = bound / largest
        return tuple(int(factor * dim) for dim in (width, height))

    def display(self, title: Optional[str] = None):
        """Use Pillow to display an image, since wand's `display` function doesn't always work"""
        with BytesIO() as fp:
            self.save(file=fp)
            pillow: pil.Image = pil.open(fp)
            pillow.show(title=title)
