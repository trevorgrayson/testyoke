import xml.etree.ElementTree as ET
from models import TestSuite, TestCase

def parse(filename):
    """ parses junit.xml, returnss suites """
    xml = ET.parse(filename)

    suites = []
    root = xml.getroot()

    if root.tag == 'testsuite':
        root = [root]

    for suite_xml in root:
        suite = TestSuite(**suite_xml.attrib)

        for case in suite_xml:
             suite.cases.append(TestCase(**case.attrib))

        suites.append(suite)
        # can impl TestSuite here.
    
    return suites
