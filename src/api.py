#
# flask server for receiving data. statsd server?
#
import os
from datetime import datetime
from persist import file as persist
import analytics


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


def get_sha(sha):
    return analytics.get_sha(sha)


def get_shas():
    return analytics.get_shas()

# TODO load all projects? 
# need to load on request?
on_load('testharness') 
