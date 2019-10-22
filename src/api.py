#
# flask server for receiving data. statsd server?
#
import os
from datetime import datetime
from persist import file as persist
from analytics.mem import Analytics

ANA = Analytics()


def receive_report(suites, project=None, sha=None):
    persist.save(suites, project, sha)
    # ANA.add_outcomes(suites)

    return True

       
def get_stats(project, **options):
    return persist.load(project, **options)
