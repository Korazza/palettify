from utils import hex_to_rgb


def test_hex_to_rgb():
    assert hex_to_rgb("#515151") == [81, 81, 81]
