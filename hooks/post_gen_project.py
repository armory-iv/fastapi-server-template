"""Post-generation hook: write MIT LICENSE, initialize git repo, print next steps."""

from __future__ import annotations

import datetime
import subprocess
import sys
from pathlib import Path

AUTHOR_NAME = "{{cookiecutter.author_name}}"
PROJECT_NAME = "{{cookiecutter.project_name}}"
PROJECT_SLUG = "{{cookiecutter.project_slug}}"

MIT_LICENSE = """\
MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def write_license() -> None:
    year = datetime.date.today().year
    Path("LICENSE.md").write_text(MIT_LICENSE.format(year=year, author=AUTHOR_NAME))


def init_git() -> None:
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)


def print_next_steps() -> None:
    print(f"""
\033[32m✔\033[0m  Project "{PROJECT_NAME}" generated successfully!

Next steps:
  cd {PROJECT_SLUG}
  uv sync
  just lint
  just test
  git commit -m "feat: initial project scaffold"
""")


def main() -> None:
    if not PROJECT_NAME.strip():
        print("Error: project_name cannot be empty.", file=sys.stderr)
        sys.exit(1)
    try:
        write_license()
        init_git()
        print_next_steps()
    except subprocess.CalledProcessError as e:
        print(f"Error during post-generation setup: {e}", file=sys.stderr)
        sys.exit(1)


main()
