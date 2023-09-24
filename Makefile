# Database test data
# A repository of databases for testing purposes
# https://www.github.com/lewisevans2007/Database_test_data
# By: Lewis Evans

SCRIPTS = $(wildcard tools/*.py)
PYTHON = python3


all: $(SCRIPTS)

$(SCRIPTS):
	$(PYTHON) $@

.PHONY: all $(SCRIPTS)