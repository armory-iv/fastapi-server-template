FROM python:{{cookiecutter.python_version}}-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev
COPY src/ ./src/
EXPOSE {{cookiecutter.port}}
CMD ["uv", "run", "gunicorn", "src.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:{{cookiecutter.port}}"]
