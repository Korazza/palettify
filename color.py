from dataclasses import dataclass, field
import numpy as np

from utils import hex_to_rgb


@dataclass
class Color:
    """Class for storing a color"""

    hex: str = field(default_factory=str)
    rgb: np.ndarray[int] = field(default_factory=lambda: np.array([]))

    def __post_init__(self):
        print(self.rgb)
        if self.hex == "" and len(self.rgb) == 0:
            self.hex = "#000000"
            self.rgb = np.array([0, 0, 0])
        elif self.hex == "":
            self.hex = f"#{self.rgb[0]:x}{self.rgb[1]:x}{self.rgb[2]:x}"
        else:
            self.rgb = np.array(hex_to_rgb(self.hex))

    def __str__(self) -> str:
        return f"<Color {self.hex}>"
