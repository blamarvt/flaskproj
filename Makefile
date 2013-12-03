.PHONY: venv update-pip update-deps hello clean

SHELL := /bin/bash

venv:
	virtualenv .venv

update-pip:
	source .venv/bin/activate && \
	.venv/bin/pip install -U pip

update-deps:
	source .venv/bin/activate && \
	.venv/bin/pip install -U -r requirements.txt

hello: venv update-pip update-deps

clean:
	rm -rf .venv
	find . -name "*.pyc" -type f -exec rm {} \;
