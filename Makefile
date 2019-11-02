PROJECT:=testharness
PYTHON?=python3
PYDEPS:=venv

export FLASK_APP = testyoke/server/__init__.py
export FLASK_RUN_PORT = 7357
export HOSTNAME = localhost
export PYTHONPATH = .:$(PYDEPS)

NOW:=$(shell date +%Y%m%d%H%m%S)
JUNIT_XML:=test-results/junit-$(NOW).xml 
export VERSION_NEW = ${shell git tag -l v[0-9]* | sort -V -r | head -n1 |  awk '/v/{split($$NF,v,/[.]/); $$NF=v[1]"."v[2]"."++v[3]}1'}
export SHA =$(shell git rev-parse HEAD)$(shell [ -z "`git diff HEAD`" ] || echo "-dirty")

travis-test: compile
	mkdir -p $(PYDEPS)
	$(PYTHON) -s -m pytest --junitxml $(JUNIT_XML) || echo "with failures"

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

package:
	echo "__version__ = '$(VERSION_NEW)'" > testyoke/version/__init__.py
	$(PYTHON) setup.py sdist bdist_wheel

publish:
	$(PYTHON) -m twine upload dist/*
	git tag "$(VERSION_NEW)"
	git push --tags

clean:
	rm -rf $(PYDEPS)
	rm -rf build dist
	find . -name *.pyc -delete

docker:
	# push to docker hub


post: 
	curl -H "vc-sha: $(SHA)" -H "Content-Type: application/xml+junit" -X POST -d "@$(FILE)" http://$(HOSTNAME):$(FLASK_RUN_PORT)/projects/testharness/reports

status:
	@$(PYTHON) -m testyoke.client --project=testyoke --sha=$(SHA)
	
