<p align="center">
  <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/Korazza/palettify?color=%233b82f6&logo=python&style=flat">
  <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/Korazza/palettify/main?color=%2365a30d&label=test&logo=circleci&style=flat">
  <img alt="Coveralls" src="https://img.shields.io/coveralls/github/Korazza/palettify?color=%2365a30d&logo=coveralls&style=flat">
  <img alt="Codacy branch grade" src="https://img.shields.io/codacy/grade/0a0cccad8d79414d88671d85ed98da06/main?color=%237c3aed&logo=codacy&style=flat">
</p>

- [Installation](#installation)
  - [pip](#pip)
  - [pipenv](#pipenv)
- [Usage](#usage)
- [Adding a palette](#adding-a-palette)
  - [Single](#single)
  - [Variants](#variants)

|                                  |                                                            |
| :------------------------------: | :--------------------------------------------------------: |
|              Normal              |                    Catppuccin Macchiato                    |
|  ![normal](examples/normal.png)  | ![catppuccin-macchiato](examples/catppuccin-macchiato.png) |
|             Gruvbox              |                          Dracula                           |
| ![gruvbox](examples/gruvbox.png) |              ![dracula](examples/dracula.png)              |

A tool to match the colors of an image to a palette

## Installation

```sh
git clone https://github.com/Korazza/palettify.git
```

### pip

```sh
pip install -r requirements.txt
```

### pipenv

```sh
pipenv sync
```

## Usage

```sh
python palettify <image path>
```

## Adding a palette

### Single

To add a new palette, simply create a file in `palettes` directory like below

`Rainbow.txt`

```md
#ff6b6b
#ffd93d
#6bcb77
#4d96ff
```

### Variants

If you have multiple variants of a palette, just create a subfolder under `palettes` with all its variants in it

`Rainbow/Pastel.txt`

```md
#ff6b6b
#ffd93d
#6bcb77
#4d96ff
```
