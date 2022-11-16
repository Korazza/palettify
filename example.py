import os
import sys
import time

from PIL import Image

import palettify.config as config
import palettify.palettes_loader as palettes_loader
from palettify import palettify_image


def main(args: list[str], palettes_path: str = config.PALETTES_DIR):
    if len(args) <= 0 or len(args) >= 2:
        print("Usage: example.py path/to/image")
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


if __name__ == "__main__":
    main(sys.argv[1:])
