# Design Patterns

Showcasing the 23 classic GoF design patterns in Python.

## Setup

After forking the repository, setup all necessary requirements and pre-commit hooks locally:

```bash
poetry install
poetry run pre-commit install
```

## Generating UML

Pyreverse will generate UML diagrams of the classes written in Python:

```bash
pyreverse -o png <path_to_src>
```