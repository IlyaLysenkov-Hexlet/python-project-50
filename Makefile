lint:
    poetry run ruff check --fix .

test:
	pytest

test:
	poetry run pytest -v

test-cov:
	coverage run -m pytest
	coverage xml
