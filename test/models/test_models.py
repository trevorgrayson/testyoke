from models import ProjectState


class TestModels:
    def test_project_state(self):
        state = ProjectState(
            passes=0,
            fails=0
        )

        assert state.has_failed == False

    def test_project_state_has_failed(self):
        state = ProjectState(
            passes=0,
            fail=1
        )

        assert state.has_failed == True

    def test_project_state_is_flaky(self):
        state = ProjectState(
            passes=1,
            fail=1
        )

        assert state.flaky == True

