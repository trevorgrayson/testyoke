from testyoke.stat import project


class TestProject:
    def test_project_name(self):
        assert project.project_name() == 'testyoke'

