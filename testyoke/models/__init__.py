PASS, FAIL = 'pass', 'fail'
TESTS_NAME = 'tests'

class TestSuite:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

        self.cases = kwargs.get('cases', [])

        self.errors = int(kwargs.get('errors', 0))
        self.failures = int(kwargs.get('failures', 0))
        self.skipped  = int(kwargs.get('skipped', 0))
        self.tests = int(kwargs.get('tests', 0))
        self.time = float(kwargs.get('', 0.0))

    @property
    def to_dict(self):
        return {
            'name': self.name,
            'time': self.time
        }


class TestCase:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.classname = kwargs.get('classname')
        self.file = kwargs.get('file')
        self.line = kwargs.get('line')
        self.time = kwargs.get('time')
        self.latest_pass = kwargs.get('latest_pass')
        self.sha = kwargs.get('sha')

        # TODO get message "./failure/@message"
        self.message = kwargs.get('message')
        self.trace = kwargs.get('trace')

        self.line = kwargs.get('line')
        if self.line is not None:
            self.line = int(self.line)

        self.is_flaky = kwargs.get('flaky')
        self.is_regressive = kwargs.get('regressive')

    @property
    def ident(self):
        return self.name.lower().replace(" ", "_")

    @property
    def did_fail(self):
        return self.message is not None

    @property
    def to_dict(self):
        return {
            'name': self.name,
            'file': self.file,
            'classname': self.classname,
            'line': self.line,
            'time': self.time,
            'message': self.message,
            'trace': self.trace,
        }


class TestReport:
    def __init__(self, **kwargs):
        self.subject = kwargs.get('case')
        self.cases = kwargs.get('cases')
        self.passes = kwargs.get('passes')  # number
        self.fails = kwargs.get('fails')  # list of failures. compare exceptions?
        self.latest = kwargs.get('latest')

    @property
    def pass_rate(self):
        fails = float(len(self.fails))
        passes = float(self.passes)

        return (passes-fails)/passes

    # def is_bullshit
    # def is_recurring
    # def is_flaky

    # def depends_on_service

    def to_dict(self):
        return {
            'pass_rate': self.pass_rate,
            # 'latest': {
            #     'timestamp': self.latest.timestamp,
            #     'sha': self.latest.sha
            # }
        }


class ProjectState:
    def __init__(self, **kwargs):
        self.sha = kwargs.get('sha')
        # self.status = kwargs.get('status')
        self.passes = kwargs.get('passes', kwargs.get(PASS, 
            kwargs.get(TESTS_NAME, {}).get('passes', 0)))
        self.fails = kwargs.get('fails', kwargs.get(FAIL, 
            kwargs.get(TESTS_NAME, {}).get('fails', 0)))

        self.failed = self.fails > 0

    @property
    def clean(self):
        """ Has never failed """
        return self.passes > 0 and self.fails == 0

    @property
    def flaky(self):
        """ Has both passed and failed """
        return self.passes > 0 and self.fails > 0

    @property
    def broken(self):
        """ Only failed """
        return self.passes == 0 and self.fails > 0

    @property
    def classification(self):
        if self.clean:
            return 'clean'
        elif self.flaky:
            return 'flaky'
        elif self.broken:
            return 'broken'
        else:
            return 'untested'

    @property
    def to_dict(self):
        return {
            'sha': self.sha, 
            TESTS_NAME: {
                'passes': self.passes,
                'fails': self.fails
            },
            'failed': self.failed,
            'nature': self.classification
        }

    def __repr__(self):
        return "nature: %s.  fails %s, passes %s" % (
            self.classification, self.fails, self.passes
        )
