import os
from json import dumps, loads
from datetime import datetime
from collections import defaultdict
from models import TestSuite, TestCase


HISTORY_FILE = os.path.join(
    os.environ.get("HOME", ''), '.test-harness/'
)

def history_file(project):
    return HISTORY_FILE + project

def save(suites, project="default", sha=None):
    try:
        os.mkdir(HISTORY_FILE)
    except FileExistsError:
        pass
    # mkdir -p
    with open(history_file(project), 'a') as fp:
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

def load(project):
    results = defaultdict(dict)

    with open(history_file(project), 'r') as fp:
        for line in fp:
            data = loads(line)
            request = data['request']
            suite = TestSuite(**data.get('suite', {}))
            case = TestCase(**data)
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
