from rut.utils import run_r_command


def install_remotes():
    cmd = ["if (!require(remotes)) {install.packages('remotes', repos='http://cloud.r-project.org/') library(remotes)}"]
    cmd = "".join(cmd)
    run_r_command(cmd)
