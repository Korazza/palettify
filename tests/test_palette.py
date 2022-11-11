import os
import numpy as np
import pytest


import config
import palette
import color


SEP = "/"
TESTS_DIR = "tests"

TEST_PALETTE_COLORS_PATH = f"{TESTS_DIR}/test_palette.txt"
TEST_PALETTE_COLORCUBE_PATH = f"{TESTS_DIR}/test_palette.npz"
TEST_PALETTE_COLORS_NONCACHED_PATH = f"{TESTS_DIR}/test_palette_noncached.txt"

TEST_PALETTE_WRONG_1_COLORS_PATH = f"{TESTS_DIR}/test_palette_wrong_1.txt"
TEST_PALETTE_WRONG_2_COLORS_PATH = f"{TESTS_DIR}/test_palette_wrong_2.txt"


def test_palette(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)

    assert test_palette.name == "test palette"
    assert test_palette.colors_path == TEST_PALETTE_COLORS_PATH
    assert test_palette.colorcube_path == TEST_PALETTE_COLORCUBE_PATH
    assert len(test_palette.colors_rgb) == 0


def test_palette_load_colors(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)
    test_palette.load_colors()

    assert test_palette.size == 2
    assert str(test_palette) == "<Palette test palette (2 colors)>"
    assert (test_palette.colors_rgb == [[0, 0, 0], [255, 255, 255]]).all()


def test_palette_get_colorcube(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)

    colorcube = test_palette.load_colorcube()

    assert colorcube.size == 3 * 256**3


def test_palette_wrong_load_colors(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette_wrong_1 = palette.Palette(TEST_PALETTE_WRONG_1_COLORS_PATH)
    with pytest.raises(Exception):
        test_palette_wrong_1.load_colors()

    test_palette_wrong_2 = palette.Palette(TEST_PALETTE_WRONG_2_COLORS_PATH)
    with pytest.raises(Exception):
        test_palette_wrong_2.load_colors()


def test_nearest_color(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)
    test_palette.load_colors()

    nearest_color_to_dimgray = test_palette.get_nearest_color(
        color.Color(rgb=[105, 105, 105])
    )

    nearest_color_to_gray = test_palette.get_nearest_color(
        color.Color(rgb=[128, 128, 128])
    )

    nearest_color_to_lightgray = test_palette.get_nearest_color(
        color.Color(rgb=[211, 211, 211])
    )

    assert nearest_color_to_dimgray.hex == "#000000"
    assert nearest_color_to_gray.hex == "#ffffff"
    assert nearest_color_to_lightgray.hex == "#ffffff"


def test_calculate_colorcube(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)
    test_palette.load_colors()

    colorcube_begin = 0
    colorcube_end = 1
    colorcube_size = colorcube_end - colorcube_begin + 1
    colorcube = test_palette.calculte_colorcube(
        begin=colorcube_begin, end=colorcube_end
    )

    assert colorcube.size == 3 * colorcube_size**3
    assert (colorcube[0][0][0] == [0, 0, 0]).all()
    assert (colorcube[0][0][1] == [0, 0, 0]).all()
    assert (colorcube[0][1][0] == [0, 0, 0]).all()
    assert (colorcube[0][1][1] == [0, 0, 0]).all()
    assert (colorcube[1][0][0] == [0, 0, 0]).all()
    assert (colorcube[1][0][1] == [0, 0, 0]).all()
    assert (colorcube[1][1][0] == [0, 0, 0]).all()
    assert (colorcube[1][1][1] == [0, 0, 0]).all()

    colorcube_begin = 127
    colorcube_end = 128
    colorcube_size = colorcube_end - colorcube_begin + 1
    colorcube = test_palette.calculte_colorcube(
        begin=colorcube_begin, end=colorcube_end
    )

    assert (colorcube[0][0][0] == [0, 0, 0]).all()
    assert (colorcube[0][0][1] == [0, 0, 0]).all()
    assert (colorcube[0][1][0] == [0, 0, 0]).all()
    assert (colorcube[0][1][1] == [255, 255, 255]).all()
    assert (colorcube[1][0][0] == [0, 0, 0]).all()
    assert (colorcube[1][0][1] == [255, 255, 255]).all()
    assert (colorcube[1][1][0] == [255, 255, 255]).all()
    assert (colorcube[1][1][1] == [255, 255, 255]).all()

    colorcube_begin = 254
    colorcube_end = 255
    colorcube_size = colorcube_end - colorcube_begin + 1
    colorcube = test_palette.calculte_colorcube(
        begin=colorcube_begin, end=colorcube_end
    )

    assert (colorcube[0][0][0] == [255, 255, 255]).all()
    assert (colorcube[0][0][1] == [255, 255, 255]).all()
    assert (colorcube[0][1][0] == [255, 255, 255]).all()
    assert (colorcube[0][1][1] == [255, 255, 255]).all()
    assert (colorcube[1][0][0] == [255, 255, 255]).all()
    assert (colorcube[1][0][1] == [255, 255, 255]).all()
    assert (colorcube[1][1][0] == [255, 255, 255]).all()
    assert (colorcube[1][1][1] == [255, 255, 255]).all()


def test_cached_cache_colorcube(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)

    assert test_palette.cache_colorcube() is False


def test_noncached_cache_colorcube(monkeypatch: pytest.MonkeyPatch):
    def fake_colorcube():
        return [0]

    def fake_savez_compressed(_, color_cube=None):
        return color_cube

    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)
    monkeypatch.setattr(np, "savez_compressed", fake_savez_compressed)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_NONCACHED_PATH)
    test_palette.calculte_colorcube = fake_colorcube

    assert test_palette.cache_colorcube() is True


def test_log(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture):
    monkeypatch.setattr(os, "sep", SEP)
    monkeypatch.setattr(config, "PALETTES_DIR", TESTS_DIR)

    test_palette = palette.Palette(TEST_PALETTE_COLORS_PATH)

    test_palette.log("Test")
    out, err = capfd.readouterr()

    assert out == f"[{test_palette.name}] Test\n"
    assert err == ""
