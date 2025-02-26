.PHONY: run-server migrate makemigrations run-migrate start-tailwind build-tailwind

PYTHON = python
MANAGE = $(PYTHON) manage.py

run-server:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run-migrate:
	$(MAKE) makemigrations && $(MAKE) migrate

start-tailwind:
	${MANAGE} tailwind start
