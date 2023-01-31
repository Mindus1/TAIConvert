import json
import pathlib

import click

from taiconvert.utils import extract_character


@click.command(name="convert")
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=pathlib.Path, dir_okay=False),
    nargs=-1,
    required=True,
)
def convert(files: tuple[pathlib.Path]):
    """
    Convert a TavernAI character image to JSON.
    """
    # Convert the tavern character images to pygmalion JSON
    click.echo("Converting TavernAI characters to Pygmalion JSON...")
    for file_path in files:
        # Extract the character JSON, beautify it and save it to a file.
        character_json = extract_character(file_path)
        click.echo(f"Converting {file_path.name}...")
        tavernai_character = json.loads(character_json)
        pygmalion_character = {
            "char_name": tavernai_character["name"],
            "char_persona": tavernai_character["description"],
            "char_greeting": tavernai_character["first_mes"],
            "world_scenario": tavernai_character["scenario"],
            "example_dialogue": tavernai_character["mes_example"],
        }
        pygmalion_character = json.dumps(pygmalion_character, indent=4)
        with open(file_path.with_suffix(".webui.json"), "w") as file:
            file.write(pygmalion_character)
        click.echo(f"Saved {file_path.with_suffix('.webui.json').name}")
    click.echo("Done!")
