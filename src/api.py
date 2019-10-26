#
# flask server for receiving data. statsd server?
#
import os
from datetime import datetime
from persist import file as persist
import analytics


def receive_report(suites, project=None, sha=None):
    persist.save(suites, project, sha)

    # TODO needs to happen here, and on load of file
    for suite in suites:
        for case in suite.cases:
            analytics.analyze_test(case, suites)

    return True

       
def get_stats(project, **options):
    return persist.load(project, **options)


def get_sha(sha):
    return analytics.get_sha(sha)

def get_shas():
    return analytics.get_shas()
