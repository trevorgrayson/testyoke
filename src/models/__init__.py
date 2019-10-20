class TestSuite:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

        self.cases = kwargs.get('cases', [])

        self.errors = int(kwargs.get('errors', 0))
        self.failures = int(kwargs.get('failures', 0))
        self.skipped  = int(kwargs.get('skipped', 0))
        self.tests = int(kwargs.get('tests', 0))
        self.time = float(kwargs.get('', 0.0))


class TestCase:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.classname = kwargs.get('classname')
        self.file = kwargs.get('file')
        self.time = kwargs.get('time')

        self.line = kwargs.get('line')
        if self.line is not None:
            self.line = int(self.line)

