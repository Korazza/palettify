def hex_to_rgb(color_hex: str) -> list[int]:
    return [int(color_hex.lstrip("#")[i : i + 2], 16) for i in [0, 2, 4]]
