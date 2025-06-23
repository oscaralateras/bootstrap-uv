import click
import toml
import os
import json
import traceback


@click.command("version", help="Show the version")
def version():
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")) as f:
            pyproject = toml.load(f)

        info = {
            "name": pyproject["project"]["name"],
            "version": pyproject["project"]["version"],
        }
        click.echo(json.dumps(info, indent=2))
    except Exception as e:
        traceback.print_exc()
        click.echo(f"An error occurred: {str(e)}", err=True)
