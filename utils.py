def hex_to_rgb(hex: str) -> list[int, int, int]:
    return [int(hex.lstrip("#")[i : i + 2], 16) for i in [0, 2, 4]]
