import builtins
import os
from PIL import Image
import numpy as np
import pytest


import config
import palette
import palettify


SEP = "/"
TESTS_DIR = "tests"

TEST_PALETTE_COLORS_PATH = f"{TESTS_DIR}/test_palette.txt"
TEST_PALETTE_PATH = f"{TESTS_DIR}/test_palette"
TEST_IMAGE_PATH = f"{TESTS_DIR}/test_image.png"


def test_palettify_image(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)
    test_palette.load_colors()

    image = Image.open(TEST_IMAGE_PATH)

    image_output = palettify.palettify_image(test_palette, image)

    assert image_output.shape == np.asarray(image).shape
    assert np.isin(test_palette.colors_rgb, image_output).all()


def test_main(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    monkeypatch.setattr(Image.Image, "save", lambda *_: "saved")

    with pytest.raises(SystemExit) as e:
        palettify.main([TEST_IMAGE_PATH], palettes_path=TEST_PALETTE_PATH)
    assert e.type == SystemExit
    assert e.value.code == 0


def test_main_wrong_usage(
    monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture
):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)
    monkeypatch.setattr(builtins, "input", lambda _: "1")

    with pytest.raises(SystemExit) as e:
        palettify.main([], palettes_path=TEST_PALETTE_PATH)
    out, err = capfd.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert out == "Usage: palettify.py <image path>\n"
    assert err == ""

    with pytest.raises(SystemExit) as e:
        palettify.main([""], palettes_path=TEST_PALETTE_PATH)
    out, err = capfd.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert out == 'Image "" does not exist\n'
    assert err == ""

    monkeypatch.setattr(builtins, "input", lambda _: "100")

    with pytest.raises(SystemExit) as e:
        palettify.main([TEST_IMAGE_PATH], palettes_path=TEST_PALETTE_PATH)
    out, err = capfd.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert out.splitlines()[-1] == "Palette 100 not in range 1-1"
    assert err == ""
