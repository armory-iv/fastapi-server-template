# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Prerequisites

- [Python {{cookiecutter.python_version}}+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [just](https://just.systems/man/en/packages.html)

## Getting Started

    just install
    just test

## Commands

| Command | Description |
|---|---|
| `just install` | Install all dependencies |
| `just lint` | Run pre-commit hooks (ruff + mypy) |
| `just test` | Run tests with coverage |
| `just coverage` | Run tests and open HTML coverage report |
| `just version-check` | Preview the next version bump |

## API

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/health` | GET | Returns `{"status": "ok", "version": "..."}` |

## Docker

    docker build -t {{cookiecutter.project_slug}} .
    docker run -p {{cookiecutter.port}}:{{cookiecutter.port}} {{cookiecutter.project_slug}}

## Project Structure

    src/
    ├── main.py          # FastAPI app factory
    ├── api/             # Route handlers
    │   └── v1/          # API version 1
    ├── config/          # Settings, logging, constants
    ├── schemas/         # Pydantic models
    └── services/        # Business logic
    tests/               # pytest test suite
