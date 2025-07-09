install:
	poetry install

lint:
	poetry run ruff check --fix .

test:
	poetry run pytest -v

test-cov:
	poetry run coverage run -m pytest
	poetry run coverage xml -o coverage.xml

check:
	make lint
	make test
