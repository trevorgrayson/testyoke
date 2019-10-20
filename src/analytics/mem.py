#
# local in mem storage
# desigining this for one suite presently, doesn't scale
#
# need to hash by project, node, test, time
from datetime import datetime


class Analytics:
    def __init__(self):
        self.runs = 0
        self.fails = 0
        self.last_pass = None
        self.failures = []

    def add_outcomes(self, suites):
        failures = []

        for suite in suites:
            for case in suite.cases:
                self.runs = self.runs + 1

                if case.did_fail:
                    failures.append(case)
                    self.fails = self.fails + 1

        if not failures:
            self.last_pass = datetime.now()  # should be from request

        self.failures = failures

    @property
    def to_dict(self):
        return {
            'runs': self.runs
        }
