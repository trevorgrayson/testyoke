#
# provide analytics on shas
#
#
from collections import defaultdict
from models import ProjectState


PASS, FAIL = 'pass', 'fail'

class Analyzer:
    def __init__(self):
        self.shas = defaultdict(dict)

    def analyze(self, case, suite=None, **options):
        status = FAIL if case.did_fail else PASS
        if not self.shas[case.sha].get(status):
            self.shas[case.sha][status] = 0

        self.shas[case.sha][status] += 1

    def all(self):
        return self.shas

    def get(self, sha):
        """
        given `sha`

        does it pass? has it ever failed?
        flaky?
        """
        sha = self.shas.get(sha)

        if sha is None:
            return sha

        return ProjectState(
            sha=sha,
            status='fail' if sha.get(FAIL, 0) > 0 else 'pass'
        )

    # def save(self):
    # def load(class):

