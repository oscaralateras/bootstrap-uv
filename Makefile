.PHONY: lint format version sync install-dev hello calc test
SHELL := /bin/bash
CLI := cli.py
NUM1 ?= 1
NUM2 ?= 2

hooks:	.git/hooks/pre-commit

.git/hooks/pre-commit: hooks/pre-commit
	@echo "Installing hooks..."
	@cp $? $@

install:
	@echo "Installing dependencies..."
	@uv pip install -e .

install-dev:
	@echo "Installing dev dependencies..."
	@uv pip install -e ".[dev]"

sync:
	@echo "Syncing dependencies..."

lint:
	@echo "Running linter..."
	@uv run ruff check .

lint-fix:
	@echo "Running linter with --fix..."
	@uv run ruff check . --fix

format:
	@echo "Running formatter..."
	@uv run black .

version:
	@uv run python ${CLI} version

hello:
	@uv run python ${CLI} hello

calc:
	@uv run python ${CLI} calc --num1 $(NUM1) --num2 $(NUM2)

test:
	@uv run python ${CLI} test

pandas1:
	@uv run python ${CLI} pandas1 --file="$(FILE)" --mode="$(MODE)"
