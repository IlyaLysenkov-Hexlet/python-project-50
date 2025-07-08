install:
	poetry install

lint:
	poetry run ruff check --fix .

test:
	poetry run pytest -v

test-cov:
	coverage run -m pytest
	coverage xml
