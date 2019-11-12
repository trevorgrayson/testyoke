import os


def project_name():
    """ best guess at project name
        requires PWD to be in root of project
    """
    return os.getcwd().split('/')[-1]
    
