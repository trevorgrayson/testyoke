from testyoke.models import TestSuite, TestCase
from testyoke.persist import file as persist


class TestFile:

    def test_saves_and_retrieves(self):
        suite = TestSuite()
        suite.cases = [
            TestCase(),
            TestCase()
        ]

        persist.save([suite], 'test-suite')
        # TODO: serialize testcase \n

