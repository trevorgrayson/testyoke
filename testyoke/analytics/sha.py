#
# provide analytics on shas
#
#
from collections import defaultdict
from testyoke.models import ProjectState


PASS, FAIL = 'pass', 'fail'

class Analyzer: # inherits from GenericAnalyzer
    def __init__(self):
        self.shas = defaultdict(dict)
        self.real_shas = defaultdict(ProjectState)

    def analyze(self, case, suite=None, **options):
        # this should not be counting all tests.
        status = FAIL if case.did_fail else PASS
        if not self.shas[case.sha].get(status):
            self.shas[case.sha][status] = 0

        self.shas[case.sha][status] += 1

    def all(self):
        return self.shas

    def get(self, sha):
        """ given `sha` """
        state = self.shas.get(sha, {})

        if state is None:
            return None

        state = ProjectState(**{**state, **{'sha': sha}})
        return state

    @property
    def has_sha(self, sha):
        return self.shas.get(sha) is not None

    # def save(self):
    # def load(class):

