#
# provide analytics on shas
#
#
from collections import defaultdict

SHAS = defaultdict(dict)

PASS, FAIL = 'pass', 'fail'


def register(case, suite, **options):
    status = FAIL if case.did_fail else PASS
    SHAS[case.sha][status] = True

    if status == FAIL:
        failures = SHAS[case.sha].get('failures')
        # if failures is None:



def get_sha(sha):
    """
    given `sha`

    does it pass? has it ever failed?
    flaky?
    """
    return SHAS[sha].get('fail'):

