# rut

A cli of r utilities aimed at package and .Rprofile management.

## Dependenciecs

`rut` depends on R and python3 ([poetry](https://poetry.eustace.io/docs/#installation) and [click](https://palletsprojects.com/p/click/)).

## Installation

Currently, this project is not on pypi, but you can install using the below
instructions if you have poetry installed.

```console
$ git clone https://github.com/datasnakes/rut.git
$ cd rut
$ poetry build
$ pip install dist/rut-0.1.0-py3-none-any.whl
```

## Usage

The current implementation of `rut` uses R's [remotes](https://github.com/r-lib/remotes) package to install packages.

Soon, [jetpack](https://github.com/datasnakes/jetpack) will be integrated to allow for better global management of user packages and in the future,
local/project package management.

### Using R's remotes package

`rut install cran` allows installation using the default/global CRAN repository.
Additionally, the user may pass a different repository to `-r`.

```console
$ rut install cran ggpubr
Running in R: remotes::install_cran(c('ggpubr'), repos='http://cloud.r-project.org/')
```

For help with `rut install cran`, type `rut install cran --help`.

```console
$ rut install cran --help
Usage: rut install cran [OPTIONS] [PACKAGES]...

  Install packages from CRAN.

  Specify versions using the following format: pkgA=1.4 pkgB=2.1

Options:
  -r, --repos TEXT    CRAN repository
  -f, --force TEXT    Force install package
  -u, --upgrade TEXT  Upgrade out-of-date packages
  --help              Show this message and exit.
```

## Maintainers

* Rob Gilmore
* Bruno Grande
* Shaurita Hutchins
* Hamid Younesy
