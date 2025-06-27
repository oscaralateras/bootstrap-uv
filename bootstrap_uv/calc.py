import click
import json
import os
import toml

@click.command("calc", help="calculator")
def calc():
    """Say hello, this is the calculator."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")) as f:
            pyproject = toml.load(f)
            version = pyproject["project"]["version"]

        info = {
            "message": "Hello, this is the calculator",
            "version": version
        }
        click.echo(json.dumps(info, indent=2))
    except Exception as e:
        click.echo(f"Error getting version: {str(e)}", err=True)
        raise
