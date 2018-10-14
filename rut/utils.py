from shutil import which
from os.path import exists
from subprocess import run


def in_path(program):
    """Check if R is available in PATH."""
    return which(program) is not None


def run_r_command(cmd, program="R"):
    """Run R command."""
    if not exists(program) and not in_path(program):
        raise Exception(f"{program} does not exists, nor is it available "
                        "in the PATH environment variable.")
        process = run([program, "-e", cmd])
        return process


def to_vector(iterable):
    """Convert iterable to a R format vector."""
    vector = "', '".join(str(e) for e in iterable)
    vector = "c('" + vector + "')"
    return vector
