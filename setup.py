from setuptools import setup, find_packages
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="taiconvert",
    description="This CLI can be used to easily convert TavernAI character \\"
    "images to JSON for the different pygmalion Web-UIs.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Mindus",
    url="https://github.com/Mindus1/taiconvert",
    project_urls={
        "Issues": "https://github.com/Mindus1/taiconvert/issues",
        "CI": "https://github.com/Mindus1/taiconvert/actions",
        "Changelog": "https://github.com/Mindus1/taiconvert/releases",
    },
    license="MIT License",
    version=VERSION,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        taiconvert=taiconvert.cli:cli
    """,
    install_requires=["click", "pillow"],
    extras_require={"dev": ["black", "flake8", "autopep8", "pre-commit"]},
    python_requires=">=3.10",
)
