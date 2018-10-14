from .utils import run_r_command, to_logical, to_character, to_vector, install_r_package
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
@click.option("--force", "-f", default=False,
              help="Force install package")
@click.option("--upgrade", "-u", default=False,
              help="Upgrade out-of-date packages")
def cran(packages, repos, force, upgrade):
    """Install packages from CRAN.

    Specify versions using the following format: pkgA=1.4 pkgB=2.1
    """

    # Format values for R
    repos_fmt = to_character(repos)
    force_fmt = to_logical(force)
    upgrade_fmt = to_logical(upgrade)

    # Make sure the remotes R package is installed
    install_r_package("remotes", repos)

    # Separate packages with specified versions
    v_pkgs = []  # With versions
    unv_pkgs = []  # Without versions
    for pkg in packages:
        if "=" in pkg:
            v_pkgs.append(pkg)
        else:
            unv_pkgs.append(pkg)

    # Install unversioned packages first
    if unv_pkgs:
        unv_pkgs_fmt = to_vector(unv_pkgs)
        cmd = (f"remotes::install_cran({unv_pkgs_fmt}, repos = {repos_fmt}, "
               f"upgrade = {upgrade_fmt}, force = {force_fmt})")
        run_r_command(cmd)

    # Install/update versioned packages next
    for pkg in v_pkgs:
        package, version = pkg.split("=", 1)
        package_fmt = to_character(package)
        version_fmt = to_character(version)
        cmd = (f"remotes::install_version({package_fmt}, {version_fmt}, repos = {repos_fmt}, "
               f"upgrade = {upgrade_fmt}, force = {force_fmt})")
        run_r_command(cmd)
