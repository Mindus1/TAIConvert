import click

from taiconvert.commands import convert, extract


@click.group()
@click.version_option()
def cli():
    "This CLI can be used to easily convert TavernAI character images to JSON for the different pygmalion Web-UIs."
    pass


cli.add_command(convert, name="convert")
cli.add_command(extract, name="extract")


def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
