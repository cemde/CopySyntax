venv_name = venv
venv_activate_path := ./$(venv_name)/bin/activate
package_name = copy_syntax
cov_args := --cov $(package_name) --cov-report=term-missing
not_slow = -m "not slow"
linelength = 120

.PHONY: clean venv lint cov slowcov docs

clean:
	rm -rf ./$(venv_name)

venv:
	python3 -m venv $(venv_name) ;\
	. $(venv_activate_path) ;\
	pip install --upgrade pip setuptools wheel ;\
	pip install --upgrade -r requirements/requirements_dev.txt ;\
	pip install --upgrade -r requirements/requirements_opt.txt ;\
	pip install --upgrade -r requirements/requirements.txt

update:
	. $(venv_activate_path) ;\
	pip install --upgrade pip setuptools wheel ;\
	pip install --upgrade -r requirements/requirements_dev.txt ;\
	pip install --upgrade -r requirements/requirements.txt

lint:
	. $(venv_activate_path) ;\
	flake8 $(package_name)/ ;\
	flake8 tests/

cov:
	. $(venv_activate_path) ;\
	py.test $(cov_args) $(not_slow)

format:
	. $(venv_activate_path) ;\
	isort -rc . ;\
	autoflake -r --in-place --remove-unused-variables $(package_name)/ ;\
	autoflake -r --in-place --remove-unused-variables tests/ ;\
	black $(package_name)/ --line-length $(linelength) --skip-string-normalization ;\
	black tests/ --line-length $(linelength) --skip-string-normalization

checkformat:
	. $(venv_activate_path) ;\
	black $(package_name)/ --line-length $(linelength) --skip-string-normalization --check ;\
	black tests/ --line-length $(linelength) --skip-string-normalization --check

test:
	. $(venv_activate_path) ;\
	pytest tests/

coveragebadge:
	. $(venv_activate_path) ;\
	coverage-badge -o .github/workflows/covbadge.svg

typechecking:
	. $(venv_activate_path) ;\
	mypy $(package_name)/ ;\
	mypy tests/

docs:
	. $(venv_activate_path) ;\
	cd docs/ ;\
	sphinx-apidoc -o . ../copy_syntax ;\
	sphinx-build -b html . build

publishdocs:
	cp -r docs/build/* pages/