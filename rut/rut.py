from .utils import run_r_command, to_vector
import click


@click.group()
def rut():
    pass


@rut.group()
def install():
    pass


@install.command()
@click.argument("packages", type=str, nargs=-1)
@click.option("--repos", "-r", default="http://cloud.r-project.org/",
              help="CRAN repository")
def cran(packages, repos):
    """Install packages from CRAN."""
    vector = to_vector(packages)
    cmd = ["remotes::install_cran(", vector, ", repos='", repos, "')"]
    cmd = "".join(cmd)
    click.echo(f"Running in R: {cmd}")
    run_r_command(cmd)
