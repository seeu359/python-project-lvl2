install:
	poetry install
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

pyt:
	pytest
