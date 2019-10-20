PROJECT:=testharness
PYTHON?=python3
PYDEPS:=venv

export FLASK_APP = src/server.py
export FLASK_RUN_PORT = 7357
export PYTHONPATH = src:$(PYDEPS)

NOW:=$(shell date +%Y%m%d%H%m%S)
JUNIT_XML:=test-results/junit-$(NOW).xml 
GIT_SHA:=$(shell git rev-parse HEAD)$(shell [ -z "`git diff HEAD`" ] || echo "-dirty") 

test: compile
	mkdir -p $(PYDEPS)
	$(PYTHON) -s -m pytest --junitxml $(JUNIT_XML) || echo "with failures"
	curl -H "vc-sha: $(GIT_SHA)" -H "Content-Type: application/xml+junit" -X POST -d @$(JUNIT_XML) http://localhost:$(FLASK_RUN_PORT)/projects/testharness/reports

compile: $(PYDEPS)
$(PYDEPS): requirements.txt
	$(PYTHON) -m pip install -t $(PYDEPS) -r requirements.txt
	touch $(PYDEPS)

server: compile
	flask run

clean:
	rm -rf $(PYDEPS)
	find . -name *.pyc -delete

post: 
	curl -H "vc-sha: $(GIT_SHA)" -H "Content-Type: application/xml+junit" -X POST -d "@$(FILE)" http://localhost:$(FLASK_RUN_PORT)/projects/testharness/reports

