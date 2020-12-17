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

    def spin(self, angle: int, delay: int):
        """Animate the image as a single spin

        Args:
            angle (int): The angle per frame (deg)
            delay (int): The delay between frames (100ths of a second)
        """
        self.dispose = "previous"
        self.delay = delay
        for angle in range(0, 360 - angle, angle):
            with self.clone() as frame:
                frame.distort("scale_rotate_translate", (angle,))
                self.sequence.append(frame)
