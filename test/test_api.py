from testyoke import api
from testyoke.models import TestSuite, TestCase

PROJECT = 'default'

class TestApi:
    def test_receives_report(self):
        suites = [
            TestSuite()
        ]

        result = api.receive_report(suites, PROJECT)
        assert result
        
    def test_get_stats(self):
        result = api.get_stats(PROJECT)

        assert result['runs'] == {}
        
