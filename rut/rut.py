import click

@click.command()
@click.option('--test', '-t', default='', help='What is this?')
def cli():
    click.echo("This is a test of the rut cli!")
