from testyoke.formats.xml import junit as parser


JUNIT_FIXTURE = 'test/fixtures/junit.xml'

class TestJunit:

    def test_read(self):
        # TODO missing <testsuites>
        xml = open(JUNIT_FIXTURE, 'r').read()
        suites = parser.parse(xml)
       
        assert suites[0].name == 'pytest' 
        assert suites[0].tests == 11

        assert suites[0].cases[0].name == 'test_benchmark'
        assert suites[0].cases[0].line == 6
        assert suites[0].cases[0].file == "tests/rsci/test_telemetry.py" 

    def test_reads_errors(self):
        # TODO missing <testsuites>
        xml = open("test-results/junit-20191020111034.xml", 'r').read()
        suites = parser.parse(xml)
       
        assert suites[0].name == 'pytest' 
        assert suites[0].tests == 6
        assert suites[0].failures == 1

        assert suites[0].cases[0].name == 'test_receives_report'

        assert suites[0].cases[3].name == 'test_read'
        assert suites[0].cases[3].did_fail
