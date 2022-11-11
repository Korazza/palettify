import os
import numpy as np

import config
import color


class Palette:
    def __init__(self, path: str):
        self.name = (
            path.replace(f"{config.PALETTES_DIR}{os.sep}", "")
            .replace(os.sep, " ")
            .replace("_", " ")
            .replace(config.COLORS_EXTENSION, "")
        )
        self.colors_path = path
        self.colorcube_path = self.colors_path.replace(
            config.COLORS_EXTENSION, config.COLORCUBES_EXTENSION
        )
        self.size = 0
        self.colors = np.array([])
        self.colors_rgb = np.array([])
        self.colors_hex = np.array([])

    def load_colors(self):
        colors = []
        with open(self.colors_path) as palette_colors_file:
            for num, _hex in enumerate(palette_colors_file, 1):
                color_hex = _hex.rstrip()
                if not color_hex.startswith("#") or len(color_hex) != 7:
                    raise Exception(
                        f'[{self.name}] Error in "{self.colors_path}" at line {num}: Colors must be in format "#000000" (got "{color_hex}")'
                    )
                if not color_hex.removeprefix("#").isalnum():
                    raise Exception(
                        f'[{self.name}] Error in "{self.colors_path}" at line {num}: Invalid color "{color_hex}"'
                    )
                colors.append(color.Color(hex=color_hex))
        self.size = len(colors)
        self.colors: np.ndarray[color.Color] = np.array(colors)
        self.colors_rgb: np.ndarray[np.ndarray[int]] = np.array(
            [color.rgb for color in self.colors]
        )

    def get_nearest_color(self, color: color.Color) -> color.Color:
        return self.colors[
            np.argmin(
                np.sqrt(
                    np.sum(
                        ((self.colors_rgb) - color.rgb) ** 2,
                        axis=1,
                    )
                )
            )
        ]

    def calculte_colorcube(self, begin: int = 0, end: int = 255) -> np.ndarray[int]:
        size = end - begin + 1
        colorcube = np.zeros(shape=[size, size, size, 3], dtype=int)
        for i, r in enumerate(range(begin, end + 1)):
            for j, g in enumerate(range(begin, end + 1)):
                for k, b in enumerate(range(begin, end + 1)):
                    colorcube[i, j, k] = self.get_nearest_color(
                        color.Color(rgb=[r, g, b])
                    ).rgb
        return colorcube

    def cache_colorcube(self) -> bool:
        if os.path.exists(self.colorcube_path):
            self.log("Color cube cached")
            return False
        self.log("Color cube not cached")
        self.log("Calculating color cube...")
        colorcube = self.calculte_colorcube()
        self.log("Color cube calculated")
        np.savez_compressed(self.colorcube_path, color_cube=colorcube)
        self.log("Color cube cached")
        return True

    def load_colorcube(self) -> np.ndarray:
        return np.load(self.colorcube_path)["color_cube"]

    def log(self, *values: object):
        print(f"[{self.name}]", *values)

    def __str__(self) -> str:
        return f"<Palette {self.name} ({self.size} colors)>"
