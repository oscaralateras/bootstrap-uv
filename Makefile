.PHONY: lint format version sync install-dev
SHELL := /bin/bash
CLI := cli.py

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
	@uv pip install -e .

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
