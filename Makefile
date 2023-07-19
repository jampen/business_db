init-db:
	psql -f sql/create-database.sql
	psql -f sql/create-department-tables.sql
	psql -f sql/create-employee-tables.sql
	psql -f sql/seed-employees.sql



PROJECT_NAME = business_db
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

## Create python interpreter environment.
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
	)

# Define utility variable to help calling Python from the virtual environment
ACTIVATE_ENV := source venv/bin/activate
PIP:=pip

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

setup-env:
	python -m venv venv

# For installing pg8000, the module for PSQL interaction
pg8000:
	$(call execute_in_env, $(PIP) install pg8000)

run:
	$(call execute_in_env, $(PYTHON_INTERPRETER) ./py/connection.py)