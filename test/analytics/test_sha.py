from pytest import fixture

from models import TestCase, ProjectState
from analytics.sha import Analyzer, PASS, FAIL

PASS_SHA = "12e45"
FAIL_SHA = "54e21"

CASES = [
    TestCase(sha=PASS_SHA),
    TestCase(sha=FAIL_SHA, message="barfed")
]


class TestSha:

    @fixture
    def sha(self):
        return Analyzer()

    def test_analyzes(self, sha):
        [sha.analyze(case) for case in CASES]
        passer = sha.get(PASS_SHA)
        failer = sha.get(FAIL_SHA)

        assert passer.status == PASS
        assert failer.status == FAIL
    
