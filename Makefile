PATH_BIN=venv/bin
PROJECT='covid19-statistics'

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'


clean: clean-build clean-pyc clean-test clean-env ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .pytest_cache
	rm -f  .coverage
	rm -fr htmlcov/
	rm -fr pylint

clean-env: ## remove environment
	rm -rf venv

lint: ## check style with pylint
	mkdir -p pylint
	${PATH_BIN}/pylint ./src/*.py > pylint/src.txt

test: ## run tests with pytest-cov and write results to txt file
	${PATH_BIN}/pytest --cov=tests --cov-report html
	echo "View results -> ./htmlcov/index.html"

install: clean ## clear and install the package to the active Python's site-packages
	virtualenv --python=python venv
	. venv/bin/activate

	${PATH_BIN}/python setup.py install
	${PATH_BIN}/python -m ipykernel install --user --name=venv

	${PATH_BIN}/python -m pip install pytest-cov
	${PATH_BIN}/python -m pip install pylint
	${PATH_BIN}/python -m pip install pre-commit

	${PATH_BIN}/pre-commit install

run-jupyter:
	${PATH_BIN}/jupyter notebook
