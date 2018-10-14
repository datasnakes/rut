from rut.utils import run_r_command


def install_remotes():
    cmd = ["if (!'remotes' %in% installed.packages()) install.packages('remotes')"]
    cmd = "".join(cmd)
    run_r_command(cmd)
