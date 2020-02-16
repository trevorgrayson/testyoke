from testyoke.cvs.git import Git


class TestGit:
    def test_sha(self):
        assert len(Git.sha()) >= 40

    # def test_is_dirty(self):
    #     assert Git.is_dirty() == ''
