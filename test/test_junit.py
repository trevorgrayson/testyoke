from formats.xml import junit as parser


JUNIT_FIXTURE = 'test/fixtures/junit.xml'

class TestJunit:

    def test_read(self):
        # TODO missing <testsuites>
        suites = parser.parse(JUNIT_FIXTURE)
       
        assert suites[0].name == 'pytest' 
        assert suites[0].tests == 11

        assert suites[0].cases[0].name == 'test_benchmark'
        assert suites[0].cases[0].line == 6
        assert suites[0].cases[0].file == "tests/rsci/test_telemetry.py" 

