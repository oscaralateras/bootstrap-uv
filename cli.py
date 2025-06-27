import click
from dotenv import load_dotenv
from bootstrap_uv.version import version
from bootstrap_uv.hello import hello


@click.group()
def cli():
    pass


cli.add_command(version)
cli.add_command(hello)

if __name__ == "__main__":
    load_dotenv()
    cli()
