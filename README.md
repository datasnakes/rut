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

### Using the jetpack cli

```console
$ rut jetpack --help
Usage: rut jetpack [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add            Add global packages using jetpack.
  install        Install jetpack.
  list-packages  List global R packages with jetpack.
  remove         Remove global packages using jetpack.

```

## Using R's remotes package

```console
$ rut install cran ggpubr
Running in R: remotes::install_cran(c('ggpubr'), repos='http://cloud.r-project.org/')
```

## Maintainers

* Rob Gilmore
* Bruno Grande
* Shaurita Hutchins
* Hamid Younesy
