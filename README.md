# kamino-chassis
Minimalist Flask foundation for rapidly building Python HTTP APIs with best practices baked in.


## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a working installation of [python](https://www.python.org/) with [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

## Setting up local environment

```bash
# install uv
$ curl -LsSf https://astral.sh/uv/install.sh | less

# run local server
$ uv run -- flask --app chassis.wsgi:application run -p 3000

# run unit tests
$ uv run -- pytest tests/

# format code
$ uv run -- black src tests
$ uv run -- isort src tests

# lint code
$ uv run -- flake8 src tests
$ uv run -- mypy src tests
```