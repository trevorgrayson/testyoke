#
# flask server for receiving data. statsd server?
#
import os
from datetime import datetime
from testyoke.persist import file as persist
from testyoke import analytics


def analyze(project, case, suite):
    analytics.analyze_test(case, suite)


def on_load(project):
    for case, suite, request in persist.all_load(project):
        analyze(project, case, suite)


def receive_report(suites, project=None, sha=None):
    persist.save(suites, project, sha)

    # TODO needs to happen here, and on load of file
    for suite in suites:
        for case in suite.cases:
            analyze(project, case, suite)

    return True

       
def get_stats(project, **options):
    return persist.load(project, **options)


def get_sha(project, sha):
    on_load('testharness')  # this will eventually have to be cached
    return analytics.get_sha(sha)


def get_shas(project):
    on_load('testharness') 
    return analytics.get_shas()

