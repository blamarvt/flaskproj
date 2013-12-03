.PHONY: venv venv-update test run clean

SHELL := /bin/bash

ifeq ($(wildcard .venv),)
venv: venv-create venv-update
venv-create:
	virtualenv .venv
else
venv:
endif

venv-update: venv
	source .venv/bin/activate && \
	pip install -U pip && \
	pip install -U -r requirements.txt && \
	pip install -U -r test-requirements.txt

test: venv
	source .venv/bin/activate && \
	nosetests

run: venv
	source .venv/bin/activate && \
	python manage.py run

clean:
	rm -rf .venv
	find . -name "*.pyc" -type f -exec rm {} \;
