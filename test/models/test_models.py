from models import ProjectState


class TestProjectState:
    def test_project_state(self):
        state = ProjectState(
            passes=0,
            fails=0
        )

        assert state.failed == False

    def test_project_state_has_failed(self):
        state = ProjectState(
            passes=0,
            fail=1
        )

        assert state.passes == 0
        assert state.fails == 1
        assert state.failed == True

        d = state.to_dict
        assert d['tests']['passes'] == 0
        assert d['tests']['fails'] == 1
        assert d['failed'] == True

    def test_project_state_is_flaky(self):
        state = ProjectState(
            passes=1,
            fail=1
        )

        assert state.flaky == True
        assert state.to_dict['nature'] == 'flaky'

