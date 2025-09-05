.PHONY: all lint format test help

# Default target executed when no arguments are given to make.
all: help

######################
# TESTING AND COVERAGE
######################

# Define a variable for the test file path.
TEST_FILE ?= tests/unit_tests

test:
	uv run pytest --disable-socket --allow-unix-socket $(TEST_FILE) -vv

test_integration:
	RUN_INTEGRATION=true uv run pytest --disable-socket --allow-unix-socket $(TEST_FILE) -vv

test_watch:
	uv run ptw . -- $(TEST_FILE)

.PHONY: test_integration


######################
# LINTING AND FORMATTING
######################

# Define a variable for Python and notebook files.
lint format: PYTHON_FILES=.
lint_diff format_diff: PYTHON_FILES=$(shell git diff --relative=. --name-only --diff-filter=d master | grep -E '\.py$$|\.ipynb$$')

lint lint_diff:
	[ "$(PYTHON_FILES)" = "" ] ||	uv run ruff format $(PYTHON_FILES) --diff
	[ "$(PYTHON_FILES)" = "" ] ||	uv run ruff check $(PYTHON_FILES) --diff
	# [ "$(PYTHON_FILES)" = "" ] || uv run mypy $(PYTHON_FILES)

format format_diff:
	[ "$(PYTHON_FILES)" = "" ] || uv run ruff format $(PYTHON_FILES)
	[ "$(PYTHON_FILES)" = "" ] || uv run ruff check --fix $(PYTHON_FILES)

unsafe_format:
	[ "$(PYTHON_FILES)" = "" ] || uv run ruff check --fix --unsafe-fixes $(PYTHON_FILES)
	

######################
# BUILD AND PACKAGE
######################

copy-typescript:
	python scripts/copy_typescript.py

build: copy-typescript
	python -m build

publish: build
	python -m twine upload dist/*

clean:
	rm -rf dist/ build/ *.egg-info

######################
# HELP
######################

help:
	@echo '===================='
	@echo '-- LINTING --'
	@echo 'format                       - run code formatters'
	@echo 'lint                         - run linters'
	@echo 'spell_check                 	- run codespell on the project'
	@echo 'spell_fix                		- run codespell on the project and fix the errors'
	@echo '-- TESTS --'
	@echo 'coverage                     - run unit tests and generate coverage report'
	@echo 'test                         - run unit tests'
	@echo 'test TEST_FILE=<test_file>   - run all tests in file'
	@echo '-- BUILD AND PACKAGE --'
	@echo 'copy-typescript              - copy TypeScript file to package directory'
	@echo 'build                        - build the package (includes copy-typescript)'
	@echo 'publish                      - build and publish to PyPI'
	@echo 'clean                        - remove build artifacts'
	@echo '-- DOCUMENTATION tasks are from the top-level Makefile --'

