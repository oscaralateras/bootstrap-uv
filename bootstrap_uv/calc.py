import click


@click.command("calc", help="calculator")
@click.option("--num1", type=int, help="First number")
@click.option("--num2", type=int, help="Second number")
def calc(num1, num2):
    """Say hello, this is the calculator."""
    try:
        result = num1 + num2
        click.echo(f"Result: {result}")

    except Exception as e:
        click.echo(f"Error getting version: {str(e)}", err=True)
        raise
