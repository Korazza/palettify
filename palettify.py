import os
import sys
import numpy as np
from PIL import Image
import time

from palettes_loader import load_palettes


def get_view(colorcube, image):
    shape = image.shape
    indices = image.reshape((-1, shape[2]))
    # pass image colors and retrieve corresponding palette color
    new_image = colorcube[indices[:, 0], indices[:, 1], indices[:, 2]]

    return new_image.reshape(shape[0], shape[1], 3).astype(np.uint8)


def main():
    args = sys.argv
    if len(args) == 1:
        print(f"Usage: {args[0]} <image path>")
        exit(1)

    image_path = args[1]
    if not os.path.exists(image_path):
        print(f'Image "{image_path}" does not exist')
        exit(1)

    palettes = load_palettes()

    print("Choose a palette")
    for i, palette in enumerate(palettes):
        print(f"{f'({i+1})'.rjust(7)} {palette.name}")
    palette_index = int(input("\n>> ")) - 1

    if palette_index < 0 or palette_index >= len(palettes):
        print(f"Palette {palette_index+1} not in range {1}-{len(palettes)}")
        exit(1)

    start = time.time()

    palette = palettes[palette_index]

    image = Image.open(image_path)
    image = np.asarray(image)

    colorcube_precalculated = np.load(palette.colorcubes_path)["color_cube"]

    result = get_view(colorcube_precalculated, image)

    output = Image.fromarray(result)
    output.save(f"output.png")

    print(f"\n[{palette.name}] Done in {round((time.time() - start), 3)}s")


if __name__ == "__main__":
    main()
