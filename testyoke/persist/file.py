import os
from json import dumps, loads
from datetime import datetime
from collections import defaultdict

from testyoke.models import TestSuite, TestCase


HISTORY_FILE = os.path.join(
    os.environ.get("HOME", ''), '.testyoke/'
)

RESULTS_FILE = 'results'


def history_file(project, filename):
    # TODO """ clean up dir concat """
    return HISTORY_FILE + project + "/" + filename


def bootstrap(project):
    # TODO check if dir exists
    try:
        if not os.path.exists(HISTORY_FILE):
            os.mkdir(HISTORY_FILE)
        if not os.path.exists(HISTORY_FILE + project):
            os.mkdir(HISTORY_FILE + project)

        results = history_file(project, RESULTS_FILE)
        if not os.path.exists(results):
            open(results, 'w').write('')

    except FileExistsError as err:
        raise Exception("Error creating info dir %s" % str(err)) 
        pass


def save(suites, project="default", sha=None):
    bootstrap(project)
    with open(history_file(project, RESULTS_FILE), 'a') as fp:
        for suite in suites:
            for case in suite.cases:
                to_write = case.to_dict
                to_write['suite'] = suite.to_dict
                to_write['request'] = {
                    'timestamp': datetime.now().isoformat(),
                }

                if sha is not None:
                    to_write['request']['sha'] = sha

                fp.write(dumps(to_write) + "\n")

def all_load(project):
    bootstrap(project)
    with open(history_file(project, RESULTS_FILE), 'r') as fp:
        for line in fp:
            data = loads(line)
            request = data['request']
            suite = TestSuite(**data.get('suite', {}))
            case = TestCase(sha=request.get('sha'), **data)

            yield (case, suite, request)

    
def load(project, **options):
    results = defaultdict(dict)

    # load
    case_suites = all_load(project)
    # filter
    if options.get('flaky'):
        case_suites = only_flaky(case_suites)

    for (case, suite, request) in case_suites:
        # TODO: this is screaming for an Aggregate class
        if results[suite.name].get(case.name) is None: 
            results[suite.name][case.name] = {
                'runs': 0, 'fails': 0, 
            }

        results[suite.name][case.name]['runs'] += 1
        if case.did_fail:
            results[suite.name][case.name]['fails'] += 1
        else:
            results[suite.name][case.name]['latest_pass'] = {
                'timestamp': request.get('timestamp'),
                'vc-sha': request.get('sha')
            }

        runs = float(results[suite.name][case.name]['runs'])
        fails = float(results[suite.name][case.name]['fails'])
        results[suite.name][case.name]['pass_rate'] = round((
            (runs-fails)/runs
        ) * 100, 2)

    return results


def only_flaky(case_suites):
    shas_pass = {}

    flaky = []

    for (case, suite, request) in case_suites:
        if case.did_fail:
            if shas_pass.get(case.sha) == True:
                flaky.append((case, suite, request))
            shas_pass[case.sha] = False

        else:
            if shas_pass.get(case.sha) == False:
                flaky.append((case, suite, request))
            shas_pass[case.sha] = True

    return flaky    


def filter(cases, **options):
    """ filter results according to `options` """
    cases = [case for case in cases]
    if options.get('flaky') is not None:
        cases = only_flaky(cases)

    return cases
