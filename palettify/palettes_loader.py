"""Module for the load_palettes function"""

import os

from . import config
from .palette import Palette


def load_palettes(path: str = config.PALETTES_DIR) -> list[Palette]:
    """
    Load all the palettes found in the `path` directory

    Parameters
    ----------
    path : str, optional
        The color from which to get the nearest palette color (default is config.PALETTES_DIR)

    Returns
    -------
    list[Palette]
        The nearest palette color to from_color
    """
    palettes: list[Palette] = []
    for palette_file in os.listdir(path):
        palette_path = os.path.join(path, palette_file)
        isdir = os.path.isdir(palette_path)
        if not palette_file.endswith(config.COLORS_EXTENSION) and not isdir:
            continue
        if isdir:
            for variant in os.listdir(palette_path):
                if not variant.endswith(config.COLORS_EXTENSION):
                    continue
                palettes.append(Palette(os.path.join(palette_path, variant)))
        else:
            palettes.append(Palette(palette_path))
    return sorted(palettes, key=lambda p: p.name)
