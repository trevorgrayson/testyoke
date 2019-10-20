# testharness

Provide insights on the outcomes of software test cases.

This project will provide resources to log the results of your test suites and aims
to add useful insight to your testing. Tests are seen as gold, and how do you prune
invalid, ineffective, or plain inaccurate test cases?

The HTTP service (which is only available for you to run locally at present) in this project
can run in the background and receive results of your test running, however you run them.

The service presently accepts junit xml, and there is a good chance your testing framework 
can export that format.  Try setting up posting the results of your tests after every run
of the suite via your build process.


## getting started

1. Run the service, check out the `service` command in this project's `Makefile`
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
  curl -H "vc-sha: $(GIT_SHA)" -H "Content-Type: application/xml+junit" -X POST -d @$(JUNIT_XML) http://localhost:$(FLASK_RUN_PORT)/projects/{your-project}/reports
```

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
POST /projects/{your-project}/reports
Content-Type: application/xml+junit
vc-sha: "GIT, or other VC sha (optional, but recommended) "


GET /projects/<project:str>

GET /projects/<project:str>/suites/<suite:str>

GET /projects/<project:str>/suites/<suite:str>/tests/<test_name:str>

```

