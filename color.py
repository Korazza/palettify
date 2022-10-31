from utils import hex_to_rgb


class Color:
    def __init__(self, hex: str):
        self.hex = hex
        self.rgb = hex_to_rgb(hex)

    def __str__(self) -> str:
        return f"<Color {self.hex}>"
