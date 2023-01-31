# TAIConvert

[![Changelog](https://img.shields.io/github/v/release/Mindus1/taiconvert?include_prereleases&label=changelog)](https://github.com/Mindus1/taiconvert/releases)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/Mindus1/taiconvert/blob/master/LICENSE)
[![PyPi Version](https://img.shields.io/pypi/v/taiconvert.svg)](https://pypi.org/project/taiconvert)

This CLI can be used to easily convert TavernAI character images to JSON for the different pygmalion Web-UIs.

## Index
- [Installation](#installation)
- [Usage](#usage)
  - [Conversion](#conversion)
  - [Extraction](#extraction)

## Installation

Install this tool using `pipx`:
```bash
$ pipx install taiconvert
```

Normal `pip` installation is also possible:
```bash
$ pip install taiconvert
```

## Usage

For help, run:
```bash
$ taiconvert --help
```

You can also use:
```bash
$ python -m taiconvert --help
```

### Conversion

To convert a single image, run:
```bash
$ taiconvert convert <path/to/image>
```

The output will be written to `<imagename>.pygmalion.json` in the same directory as the image.

To convert multiple images, run:
```bash
$ taiconvert convert <path/to/image1> <path/to/image2> <path/to/image3> ...
```

### Extraction

To extract the character json from a TavernAI character image file, run:
```bash
$ taiconvert extract <path/to/image>
```

The output will be written to `<imagename>.tavernai.json` in the same directory as the image.

To extract multiple images, run:
```bash
$ taiconvert extract <path/to/image1> <path/to/image2> <path/to/image3> ...
```

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
$ pipx install virtualenv
$ cd taiconvert
$ virtualenv .venv
$ .venv/Scripts/activate
```

Now install the dependencies and install the pre-commit hooks:
```bash
$ pip install -e '.[dev]'
$ pre-commit install
```
