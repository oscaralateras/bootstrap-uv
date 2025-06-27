import click
import json
import os
import toml

@click.command("calc", help="calculator")
def calc():
    """Say hello, this is the calculator."""
    try:
        click.echo("Hello, this is the calculator")
    except Exception as e:
        click.echo(f"Error getting version: {str(e)}", err=True)
        raise
