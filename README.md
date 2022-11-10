# palettify

<p align="center">
<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/Korazza/palettify?color=%233b82f6&style=for-the-badge">
<img alt="CircleCI" src="https://img.shields.io/circleci/build/github/Korazza/palettify/main?color=%2384cc16&label=Test&logo=circleci&style=for-the-badge">
<img alt="Coveralls" src="https://img.shields.io/coveralls/github/Korazza/palettify?color=%2384cc16&style=for-the-badge">
</p>

- [Installation](#installation "Goto installation")
  - [pip](#pip "Goto pip")
  - [pipenv](#pipenv "Goto pipenv")
- [Usage](#usage "Goto usage")
- [Adding a palette](#adding-a-palette "Goto adding-a-palette")
  - [Single](#single "Goto single")
  - [Variants](#variants "Goto variants")

|                           |                                        |
| :-----------------------: | :------------------------------------: |
|          Normal           |          Catppuccin Macchiato          |
| ![](examples/normal.png)  | ![](examples/catppuccin-macchiato.png) |
|          Gruvbox          |                Dracula                 |
| ![](examples/gruvbox.png) |       ![](examples/dracula.png)        |

A tool to match the colors of an image to a palette

## Installation

```
git clone https://github.com/Korazza/palettify.git
```

### pip

```
pip install -r requirements.txt
```

### pipenv

```
pipenv install
```

## Usage

```
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
