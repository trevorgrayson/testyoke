# testyoke client

Post new test results to the service, or get reports to make decisions.

Everytime you run a test, `POST` the result to the service.

```bash
  python -m testyoke.client --sha=`git rev-parse HEAD` --report=junit.xml
```

More formats are expected to be supported soon.  You may, of course, use your version control of choice.

### `POST` formats

Ultimately data will be collected by either testing frameworks' reporters, or by submitting reports after
tests complete.  This process must be automatic, and not be a manual submission.

#### junit xml

JUNIT.xml is one of the more prevalent formats in the space, supported by [pytest](https://docs.pytest.org/en/latest/), [scalatest](), 
and obviously in java frameworks as well.  This is the first format to be supported.

You can submit via curl/HTTP Post via the following (**Run this after your tests run**):

## Analytics

**Run this before your tests run.**

This will provide you with historical information, and if this SHA has been proven.

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

