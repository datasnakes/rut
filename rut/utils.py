from shutil import which
from os.path import exists
from subprocess import run
import click


def in_path(program):
    """Check if R is available in PATH."""
    return which(program) is not None


def run_r_command(cmd, program="R"):
    """Run R command"""
    if not exists(program) and not in_path(program):
        raise Exception(f"{program} does not exists, nor is it available "
                        "in the PATH environment variable.")
    args = [program, "--quiet", "-e", cmd]
    click.echo(f"$ {' '.join(args)}")
    process = run(args)
    return process


def install_r_package(package, repos):
    """Check if R package is installed and if not, install it.

    Returns whether the package was initially installed
    """
    package_fmt = to_character(package)
    repos_fmt = to_character(repos)
    check_proc = run_r_command(f"library({package_fmt})")
    is_installed = check_proc.returncode == 0
    if not is_installed:
        install_proc = run_r_command(f"install.packages({package_fmt}, repos = {repos_fmt})")
        if install_proc.returncode != 0:
            raise Exception("{package} didn't install correctly.")
    return is_installed


def to_logical(value):
    """Format boolean value to logical for R."""
    return "TRUE" if value else "FALSE"


def to_character(value):
    """Format string value to character for R."""
    return "'" + value + "'"


def to_vector(iterable, type="character"):
    """Convert iterable to vector for R."""
    formatters = {
        "character": to_character,
        "logical": to_logical}
    formatter = formatters[type]
    vector = ", ".join(formatter(v) for v in iterable)
    vector = "c(" + vector + ")"
    return vector
