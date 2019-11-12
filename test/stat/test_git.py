from testyoke import stat


class TestGit:

    def test_vcsha(self):
        sha = stat.vcsha()    

        assert len(sha) in [40, 46]


    # def test_not_in_git_dir(self):

    # def test_no_git(self):
