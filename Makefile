IMAGE := tgrayson/testyoke
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
	openssl aes-256-cbc -k "$(enc_key_password)" -d -md sha256 -a -in travis_key.enc -out travis_key
	echo "Host github.com" > ~/.ssh/config
	echo "  IdentityFile travis_key" >> ~/.ssh/config
	chmod 400 travis_key
	git remote set-url origin git@github.com:trevorgrayson/testyoke.git
	echo "github.com ssh-rsa ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC4hU+C8fy/itpitFhKlGvmebOY5tNm+Qt805s3YPLXNY+IL1b6dTSIMyBHsCTsy8OhljpYSaBBy7tLP4nFaF8GnDxhyKDYb48OWcKU8EFGHhP6w4VD7xu+pRACCA972cuBi/ypz6gBmdYeIIniUaJWYtpD0G2RMCU8dB4N3Y5nATDezWf8rYIeHdxtlcHF4Xn0J0rA+tTdJBxMbEFo9Vc+ynKpVei1/qM2y0Do1noGHjpZCCW7PGa3rT0Keo8Ej/1Du0BTdOpOtOVCvjriIw4h+z/QEGMxQ4a7xgZ06K80NIibZxAqxY1IyBzuGxIqZIULBEQeTZVg2nBTVHx4cPX/5H6gn6S0gmHLoB5mSn4UuRfwB1IfbyywKWkX/Q1Rj92ZcT4XvnUN/Po5Yg8x4TTZ1JxelMP6pQsv1taRd1zBiFV8FuL1FFxqWeIyFnSu+VAf2sXN6t6wpnvZNg5Q7o+dixzXWu/JGzv2FniGYqqF0CQrAbqD98dbbvV/6PyiaNUvCPvmEOZeB4uQNIy62tn30jMDcErX4glWCK+Mw/cxdpK8Sv5RIfTpr1ZtSkt8oZ91kkM1YIUhSEYzfvQEAPTnqtA3vJpk2ouu/VlUTbFpRAPtXtRxeVi6y8LzkO7kok7DKo8K0GT7EOvqBDFx0di1arl9zGc6HkRGrRyqdf1T+w== oss@ipsumllc.com" >> ~/.ssh/known_hosts
	git tag "$(VERSION_NEW)"
	git push --tags
	$(PYTHON) -m twine upload dist/*

clean:
	rm -rf $(PYDEPS)
	rm -rf build dist
	find . -name *.pyc -delete

image: 
	docker build -t $(IMAGE) .

imagePush:
	echo "$(DOCKER_PASS)" | docker login -u "$(DOCKER_USER)" --password-stdin
	docker push $(IMAGE)

docker:
	# push to docker hub


post: 
	curl -H "vc-sha: $(SHA)" -H "Content-Type: application/xml+junit" -X POST -d "@$(FILE)" http://$(HOSTNAME):$(FLASK_RUN_PORT)/projects/testharness/reports

status:
	@$(PYTHON) -m testyoke.client --project=testyoke --sha=$(SHA)
	
