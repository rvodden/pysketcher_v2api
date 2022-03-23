import nox
from nox.sessions import Session

nox.options.sessions = "lint", "tests"
nox.options.reuse_existing_virtualenvs = True
locations = "pysketcher", "tests", "noxfile.py"

main_version = ["3.8"]
supported_versions = ["3.7", "3.8", "3.9", "3.10"]


@nox.session(python=main_version)
def lint(session: Session) -> None:
    args = session.posargs or locations
    session.install(
        "darglint",
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=supported_versions)
def tests(session: Session) -> None:
    session.install(".")
    session.install("pytest")
    session.run("pytest")
