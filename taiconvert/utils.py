"""
Utility functions for the CLI
"""
import base64
import pathlib

from PIL import Image


def extract_character(image_path: pathlib.Path) -> str:
    """
    Extract the character JSON from the image.

    :param image: The path to the image
    :return: The character JSON
    """
    # Load the image
    image = Image.open(image_path)
    image.load()

    # Decrypt the BASE64 encrypted character
    character_crypted = image.info["chara"]
    character_decrypted = base64.b64decode(character_crypted).decode("utf-8")
    return character_decrypted
