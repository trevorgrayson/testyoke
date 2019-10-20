# testharness

A project to record the outcomes of software test cases, and provide insights.

## Projects

- web service
- reporters
  - scalatest
  - pytest
- cli client
- analytics
- web portal


### [web service](http://c.es/testharness/service)


```HTTP
POST /test-report
Content-Type: application/xml+scalatest

<scalatest-format/>


GET /projects/<project:str>

GET /projects/<project:str>/suites/<suite:str>

GET /projects/<project:str>/suites/<suite:str>/tests/<test_name:str>

```

### Reporters

#### scalatest

I can use, small market.

#### pytest

Frank can use, large market.
