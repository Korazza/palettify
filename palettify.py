import os
import sys
import time
from PIL import Image
import numpy as np

import palette
import palettes_loader


def palettify_image(palette: palette.Palette, image: Image.Image) -> np.ndarray:
    image = np.asarray(image)
    colorcube = palette.load_colorcube()
    shape = image.shape
    indices = image.reshape((-1, shape[2]))
    output_image = colorcube[indices[:, 0], indices[:, 1], indices[:, 2]]
    return output_image.reshape(shape[0], shape[1], 3).astype(np.uint8)


def main():
    args = sys.argv
    if len(args) == 1:
        print(f"Usage: {args[0]} <image path>")
        exit(1)

    image_path = args[1]
    if not os.path.exists(image_path):
        print(f'Image "{image_path}" does not exist')
        exit(1)

    palettes = palettes_loader.load_palettes()

    print("Choose a palette")
    for i, palette in enumerate(palettes):
        print(f"{f'({i+1})'.rjust(7)} {palette.name}")
    palette_index = int(input("\n>> ")) - 1
    print()

    if palette_index < 0 or palette_index >= len(palettes):
        print(f"Palette {palette_index+1} not in range {1}-{len(palettes)}")
        exit(1)

    start = time.time()

    palette = palettes[palette_index]
    image = Image.open(image_path)

    image_result = Image.fromarray(palettify_image(palette, image))

    image_result.save(f"output.png")

    palette.log(f"Done in {(time.time() - start):.3f}s")


if __name__ == "__main__":
    main()
