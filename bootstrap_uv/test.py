import click


@click.command("test", help="test")
def test():
    """Say this is a test command."""
    try:
        click.echo("This code is a test command")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise
