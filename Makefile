# Database test data
# A repository of databases for testing purposes
# https://www.github.com/0x4248/Database_test_data
# By: 0x4248

SCRIPTS = $(wildcard tools/*.py)
PYTHON = python3


all: $(SCRIPTS)

$(SCRIPTS):
	$(PYTHON) $@

.PHONY: all $(SCRIPTS)