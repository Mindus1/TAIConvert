import sys
import click

from taiconvert.commands import convert, extract


@click.group()
@click.version_option()
def cli():
    "This CLI can be used to easily convert TavernAI character images to JSON for the different pygmalion Web-UIs."
    pass


cli.add_command(convert, name="convert")
cli.add_command(extract, name="extract")

# Run cli function if script is frozen by pyinstaller
if getattr(sys, "frozen", False):
    cli(sys.argv[1:])
