
.PHONY: setup test format lint run-all clean

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -U pip
	. .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

test:
	. .venv/bin/activate && pytest -q

format:
	. .venv/bin/activate && black src tests

lint:
	. .venv/bin/activate && isort src tests && black --check src tests

run-all:
	. .venv/bin/activate && python scripts/run_all.py

clean:
	rm -rf output dist build .pytest_cache __pycache__
