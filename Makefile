PROJECT:=testharness
PYTHON?=python3
PYDEPS:=venv

export FLASK_APP = testyoke/server/__init__.py
export FLASK_RUN_PORT = 7357
export HOSTNAME = localhost
export PYTHONPATH = .:$(PYDEPS)

NOW:=$(shell date +%Y%m%d%H%m%S)
JUNIT_XML:=test-results/junit-$(NOW).xml 
export SHA =$(shell git rev-parse HEAD)$(shell [ -z "`git diff HEAD`" ] || echo "-dirty")

test: status compile
	mkdir -p $(PYDEPS)
	$(PYTHON) -s -m pytest --junitxml $(JUNIT_XML) || echo "with failures"
	$(PYTHON) -m testyoke.client --project=testyoke --sha=$(SHA) --report=$(JUNIT_XML)

compile: $(PYDEPS)
$(PYDEPS): requirements.txt
	$(PYTHON) -m pip install -t $(PYDEPS) -r requirements.txt
	touch $(PYDEPS)

server: compile
	$(PYTHON) -m flask run

install:
	# python3 -m pip install --user --upgrade setuptools wheel
	$(PYTHON) setup.py sdist bdist_wheel
	$(PYTHON) -m pip install --no-deps testyoke # --index-url https://test.pypi.org/simple/ 

clean:
	rm -rf $(PYDEPS)
	rm -rf build dist
	find . -name *.pyc -delete

#
# move following into cli client
#

post: 
	curl -H "vc-sha: $(SHA)" -H "Content-Type: application/xml+junit" -X POST -d "@$(FILE)" http://$(HOSTNAME):$(FLASK_RUN_PORT)/projects/testharness/reports

status:
	@$(PYTHON) -m testyoke.client --project=testyoke --sha=$(SHA)
	@echo ""
	
