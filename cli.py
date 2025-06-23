import click
from dotenv import load_dotenv
from bootstrap_uv.version import version


@click.group()
def cli():
    pass


cli.add_command(version)

if __name__ == "__main__":
    load_dotenv()
    cli()
