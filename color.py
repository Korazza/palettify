from dataclasses import dataclass
import numpy as np

from utils import hex_to_rgb


@dataclass
class Color:
    """Class for storing a color"""

    hex: str = None
    rgb: np.ndarray[int] = None

    def __post_init__(self):
        if self.hex == None and self.rgb == None:
            self.hex = "#000000"
            self.rgb = np.array([0, 0, 0])
        elif self.hex == None:
            self.hex = f"#{self.rgb[0]:x}{self.rgb[1]:x}{self.rgb[2]:x}"
        else:
            self.rgb = np.array(hex_to_rgb(self.hex))

    def __str__(self) -> str:
        return f"<Color {self.hex}>"
