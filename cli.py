import click
from dotenv import load_dotenv
from bootstrap_uv.version import version
from bootstrap_uv.hello import hello
from bootstrap_uv.calc import calc
from bootstrap_uv.test import test


@click.group()
def cli():
    pass


cli.add_command(version)
cli.add_command(hello)
cli.add_command(calc)
cli.add_command(test)

if __name__ == "__main__":
    load_dotenv()
    cli()
