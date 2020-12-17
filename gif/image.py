from typing import Tuple
import wand.image as wand


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