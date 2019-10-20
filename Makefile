PYTHON?=python2.7
PYDEPS:=venv

export PYTHONPATH = src:$(PYDEPS)

test: compile
	mkdir -p $(PYDEPS)
	$(PYTHON) -s -m pytest --junitxml test-results/junit-$(shell date +%Y%m%d%H%m%S).xml

compile: $(PYDEPS)
$(PYDEPS): requirements.txt
	$(PYTHON) -m pip install -t $(PYDEPS) -r requirements.txt
	touch $(PYDEPS)

