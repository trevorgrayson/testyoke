import xml.etree.ElementTree as ET
from testyoke.models import TestSuite, TestCase

def parse(filename, **options):
    """ parses junit.xml, ALWAYS returns suites """
    root = ET.fromstring(filename)

    suites = []

    if root.tag == 'testsuite':
        root = [root]

    for suite_xml in root:
        suite = TestSuite(**suite_xml.attrib)

        for testcase in suite_xml:
            case = TestCase(**testcase.attrib)
            case.sha = options.get('sha')

            failure = testcase.find('failure')
            case.message = failure
            if failure is not None:
                case.message = failure.attrib['message']
                case.trace = failure.text

            suite.cases.append(case)

        suites.append(suite)
        # can impl TestSuite here.
    
    return suites
