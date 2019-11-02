# testyoke

Provide insights on the outcomes of software test cases.

This project will provide resources to log the results of your test suites and aims
to add useful insights to your testing. Tests are seen as gold, but how do you prune
invalid, ineffective, or plain inaccurate test cases? With TestYoke you can:

* See the results of tests on this git sha previously. Big time savings here, by not running again.
* Flaky Tests - have both passed and failed on the present sha. There probably is a data or service dependency issue.
* Bad Tests - tests that have been failing across consecutive shas.  If these have been deployed anyways, these tests are worthless.  Prompt user to delete because they are costing the staff more than a good test is worth.
* Regressions - tests that failed, were fixed, and fail again in different shas.  Regressions are recurring issues. They may prompt priority to fix.

The HTTP service in this project can run in the background and receive results of 
your test running, however you run them.

The service presently accepts junit xml, and there is a good chance your testing framework 
can export that format.  Try setting up posting the results of your tests after every run
of the suite via your build process.


## getting started

1. Run the service.

```
make server
```

2. Everytime you run a test, `POST` the result to the service.
  - i.o.u docker

## `POST` formats

Ultimately data will be collected by either testing frameworks' reporters, or by submitting reports after
tests complete.  This process must be automatic, and not be a manual submission.

### junit xml

One of the more prevalent formats in the space, supported by [pytest](https://docs.pytest.org/en/latest/), [scalatest](), 
and obviously in java framworks as well.  This is a supported.

You can submit via curl/HTTP Post via the following:

```
  python -m testyoke.client --sha=`git rev-parse HEAD` --report=junit.xml
```

## Analytics

Run this before your tests.

```
  python -m testyoke.client --sha=`git rev-parse HEAD`
```

Example output:

```
###################################################
#
# nature: untested.  fails 0, passes 0
#
###################################################
```

### Nature

This is a classification of the SHA you are running on.

* untested - testyoke hasn't seen results from this SHA yet
* clean - testyoke has never seen a failure on this SHA
* broken - this SHA has never passed completely.
* flaky - there is at least one flaky test, defined as having passed and failed on the same SHA.

## Projects

- web service
- reporters
  - scalatest
  - pytest
  - rspec
- cli client
- analytics
- web portal


### [web service](http://c.es/testharness/service)


```HTTP
POST /projects/<project:str>/reports
Content-Type: application/xml+junit
vc-sha: "GIT, or other VC sha (optional, but recommended)"

GET /projects/<project:str>

GET /projects/<project:str>/suites/<suite:str>

GET /projects/<project:str>/suites/<suite:str>/tests/<test_name:str>

```

### Version Control SHAS

```HTTP
GET /projects/<project:str>/shas/<sha:str>

```

## Arch

API -> persist
       analyzers
