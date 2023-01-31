import json
import pathlib

import click

from taiconvert.utils import extract_character


@click.command(name="extract")
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=pathlib.Path),
    nargs=-1,
    required=False,
)
def extract(files: tuple[pathlib.Path]):
    """
    Extract a TavernAI character JSON from a character image.
    """
    # Prompt the user for the path to the character image and for the type of JSON to convert to
    click.echo("Extraction TavernAI character JSON...")
    for file_path in files:
        # Extract the character JSON, beautify it and save it to a file.
        extracted_character = extract_character(file_path)
        click.echo(f"Extracting {file_path.name}...")
        character_json = json.loads(extracted_character)
        character_json = json.dumps(character_json, indent=4)
        with open(file_path.with_suffix(".tavernai.json"), "w") as f:
            f.write(character_json)
        click.echo(f"Saved {file_path.with_suffix('.tavernai.json').name}")
    click.echo("Done!")
