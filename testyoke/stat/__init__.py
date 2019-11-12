from . import git
from . import project

# TODO ask permission to use `git`


def vcsha():
    try:
        return git.vcsha()
    except FileNotFoundError:
        pass

def project_name():
    return project.project_name()
