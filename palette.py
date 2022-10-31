import os
import numpy as np

from color import Color
from config import PALETTES_DIR, COLORS_EXTENSION, COLORCUBES_EXTENSION


class Palette:
    def __init__(self, path: str):
        self.name = (
            path.removesuffix(COLORS_EXTENSION)
            .removeprefix(PALETTES_DIR)
            .removeprefix(os.sep)
            .replace(os.sep, " ")
            .replace("_", " ")
        )
        self.colors_path = path
        self.dir = os.path.dirname(path)
        self.colorcubes_path = self.colors_path.replace(
            COLORS_EXTENSION, COLORCUBES_EXTENSION
        )
        # load colors
        self.load_colors()

        # calculate color cube if file not found
        if not os.path.exists(self.colorcubes_path):
            self.calculate_colorcube()

    def load_colors(self):
        colors_rgb = []
        with open(self.colors_path) as palette_file:
            for num, line in enumerate(palette_file, 1):
                line = line.rstrip()
                if not line.removeprefix("#").isalnum():
                    raise Exception(
                        f'[{self.name}] Error in {self.colors_path}\nline {num} | "{line}"'
                    )
                colors_rgb.append(Color(line).rgb)
        self.colors_rgb = np.array(colors_rgb)

    def calculate_colorcube(self):
        print(f"[{self.name}] Color cube not cached")
        colorcube_precalculated = np.zeros(shape=[256, 256, 256, 3])
        for i in range(256):
            print(
                f"\r[{self.name}] Processing color cube {('.' * (i % 4)).ljust(3)} {str(round(100 * i / 256, 2)).rjust(6)}%",
                end="",
            )
            for j in range(256):
                for k in range(256):
                    index = np.argmin(
                        np.sqrt(
                            np.sum(
                                ((self.colors_rgb) - np.array([i, j, k])) ** 2,
                                axis=1,
                            )
                        )
                    )
                    colorcube_precalculated[i, j, k] = self.colors_rgb[index]
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        np.savez_compressed(self.colorcubes_path, color_cube=colorcube_precalculated)
        print()

    def get_hex_colors(self) -> list[str]:
        return [color.hex for color in self.colors]

    def get_rgb_colors(self) -> list[list[int, int, int]]:
        return [color.rgb for color in self.colors]

    def __str__(self) -> str:
        return f"<Palette {self.name} ({len(self.colors)} colors)>"
