from dataclasses import dataclass, field
import numpy as np


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
            self.rgb = np.array(
                [int(self.hex.lstrip("#")[i : i + 2], 16) for i in [0, 2, 4]]
            )

    def __str__(self) -> str:
        return f"<Color {self.hex}>"
