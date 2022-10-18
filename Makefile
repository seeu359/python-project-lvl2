install:
	poetry install
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl


install-venv:
	poetry install
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

pyt:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
