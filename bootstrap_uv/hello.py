import click
import json
import os
import toml


@click.command("hello", help="Say hello")
def hello():
    """Say hello to the user."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")) as f:
            pyproject = toml.load(f)
            version = pyproject["project"]["version"]

        info = {"message": "Hello! Welcome to bootstrap-uv", "version": version}
        click.echo(json.dumps(info, indent=2))
    except Exception as e:
        click.echo(f"Error getting version: {str(e)}", err=True)
        raise
