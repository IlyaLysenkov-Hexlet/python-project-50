lint:
	uv run -- ruff check gendiff tests

test:
	uv run pytest
	
install:
	poetry install

test-cov:
	coverage run -m pytest
	coverage xml