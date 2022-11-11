"""
palettify
---------
A tool to match the colors of an image to a palette
"""
import os
import sys
import time

import numpy as np
from PIL import Image

import config
import palettes_loader
from palette import Palette


def palettify_image(palette: Palette, image: Image.Image) -> np.ndarray:
    """Get an image processed with the `palette` colors

    Parameters
    ----------
    palette : Palette
        The palette choosen to process the image
    image : Image
        The image to process

    Returns
    -------
    ndarray
        The processed image as a numpy ndarray
    """
    palette.load_colors()
    palette.cache_colorcube()
    image = np.asarray(image)
    colorcube = palette.load_colorcube()
    shape = image.shape
    indices = image.reshape((-1, shape[2]))
    output_image = colorcube[indices[:, 0], indices[:, 1], indices[:, 2]]
    return output_image.reshape(shape[0], shape[1], 3).astype(np.uint8)


def main(args: list[str], palettes_path: str = config.PALETTES_DIR):
    """The main function of palettify

    Parameters
    ----------
    args : list[str]
        The args for the program
    palettes_path : str, optional
        The path to directory from which to load the palettes (default is config.PALETTES_DIR)
    """
    if len(args) <= 0 or len(args) >= 2:
        print("Usage: palettify.py <image path>")
        sys.exit(1)

    image_path = args[0]
    if not os.path.exists(image_path):
        print(f'Image "{image_path}" does not exist')
        sys.exit(1)

    palettes = palettes_loader.load_palettes(palettes_path)

    print("Choose a palette")
    for i, palette in enumerate(palettes):
        print(f"{f'({i+1})'.rjust(7)} {palette.name}")
    palette_index = int(input("\n>> ")) - 1
    print()

    if palette_index < 0 or palette_index >= len(palettes):
        print(f"Palette {palette_index+1} not in range {1}-{len(palettes)}")
        sys.exit(1)

    start = time.time()

    palette = palettes[palette_index]
    image = Image.open(image_path)

    image_result = Image.fromarray(palettify_image(palette, image))
    image_result.save("output.png")

    palette.log(f"Done in {(time.time() - start):.3f}s")
    sys.exit(0)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
