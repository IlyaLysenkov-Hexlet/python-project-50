lint:
	ruff check gendiff formaters scripts tests

test:
	pytest

install:
	poetry install

test-cov:
	coverage run -m pytest
	coverage xml
