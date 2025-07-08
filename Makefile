lint:
	ruff check gendiff tests

test:
	pytest

install:
	poetry install

test-cov:
	coverage run -m pytest
	coverage xml
