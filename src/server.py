#
# flask server for receiving data. statsd server?
#
import os
from datetime import datetime
from models.test_run import TestRun

HISTORY_FILE = os.environ.get("HOME", '')

# need this for every test, or read from file.
STATS = {
    'runs', 0,
    'fails', 0,
    'last_pass': '0 minutes',
    'failures': []
}


def receive_run(test):
    # receive one test at a time?
    pass

def receive_batch(tests):
    failures = []
    with open(HISTORY_FILE, 'a') as fp:
        fp.write(str(tests)+"\n")

        for test in tests:
            test = TestRun(**test)
            STATS['runs'] = STATS['runs'] + 1

            if test.did_fail:
                failures.append(test)
                STATS['fails'] = STATS['fails'] + 1
       
    if not failures:
        STATS['last_pass'] = datetime.now()

    STATS['failures'] = failures

def get_stats():
    return STATS
