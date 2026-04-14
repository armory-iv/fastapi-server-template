# fastapi-server-template

A [cookiecutter](https://cookiecutter.readthedocs.io) template for production-ready FastAPI server projects.

## What it generates

Running the template scaffolds a fully wired Python project with:

- **FastAPI** app with a versioned API structure (`/api/v1/`) and a working health check endpoint
- **UV** for dependency management and virtual environments
- **Just** task runner (`install`, `lint`, `test`, `coverage`, `version-check`)
- **Docker** — single-stage UV build, ready to run with gunicorn + uvicorn workers
- **pre-commit** — ruff (lint + format) and mypy gates
- **commitizen** — semantic versioning with automatic CHANGELOG updates
- **GitHub Actions** — CI on PRs, automated version bump + tag on merge to main
- **VS Code / Cursor** — debug launch config, task runner, agents, and rules

## Requirements

- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) (`pip install cookiecutter` or `uv tool install cookiecutter`)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (for the generated project)
- [just](https://just.systems/man/en/packages.html) (for the generated project)

## Usage

```bash
cookiecutter gh:armory-iv/fastapi-server-template
```

Or locally:

```bash
cookiecutter ~/path/to/fastapi-server-template
```

You will be prompted for:

| Variable | Description | Default |
|---|---|---|
| `project_name` | Human-readable name | *(required)* |
| `project_slug` | Directory and package name (auto-derived) | slugified `project_name` |
| `description` | One-line description | `"A FastAPI server"` |
| `author_name` | Your name | `"Your Name"` |
| `author_email` | Your email | `"you@example.com"` |
| `github_username` | GitHub username or org | `"your-github-username"` |
| `python_version` | Python version (2-component, e.g. `3.13`) | `"3.13"` |
| `port` | Server port | `"8000"` |

## After generation

```bash
cd <project_slug>
uv sync
just lint
just test
git commit -m "feat: initial project scaffold"
```

## Project structure (generated)

```
<project_slug>/
├── src/
│   ├── main.py          # FastAPI app factory (entrypoint: src.main:app)
│   ├── api/v1/          # Versioned route handlers
│   ├── config/          # Settings, logging, constants
│   ├── schemas/         # Pydantic models
│   └── services/        # Business logic
├── tests/               # pytest suite (mirrors src/ structure)
├── justfile             # Dev task runner
├── Dockerfile           # Single-stage UV build
├── pyproject.toml       # Project metadata + tool config
└── .github/workflows/   # CI/CD pipelines
```
