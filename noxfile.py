import nox

@nox.session(reuse_venv=True)
def docs(session):
    session.install("sphinx", "furo", "myst-parser", "sphinx-copybutton")
    session.run("sphinx-build", "docs/source", "docs/build")

@nox.session(reuse_venv=True)
def docs_live(session):
    session.install("sphinx", "sphinx-autobuild", "furo", "myst-parser", "sphinx-copybutton")
    session.run("sphinx-autobuild", "docs/source", "docs/build/html")
