import subprocess


def vcsha():
    process = subprocess.Popen(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE)
    process.wait()
    sha_result = process.stdout
    
    process = subprocess.Popen(["git", "diff"], stdout=subprocess.PIPE)
    process.wait()
    dirty_result = process.stdout

    # TODO: -dirty
    if sha_result:

        flag = ''

        if dirty_result: 
            dirty = dirty_result.read().strip().decode("unicode_escape")
            if len(dirty) > 2:
                flag = '-dirty'

        return sha_result.read().strip().decode("unicode_escape") + flag

# TODO def project_name(): origin > url
