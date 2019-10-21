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

        # TODO get message "./failure/@message"
        self.message = kwargs.get('message')
        self.trace = kwargs.get('trace')

        self.line = kwargs.get('line')
        if self.line is not None:
            self.line = int(self.line)

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
    def to_dict(self):
        return {}

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
