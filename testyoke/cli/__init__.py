import sys
from os import path, environ
import subprocess
from testyoke import Client, get_config
from testyoke.cvs import Git
from testyoke.client import ClientException
from testyoke.view import view

XML_ARG = {
    'pytest': '--junitxml',
    'py.test': '--junitxml',
    'rspec': '--format RspecJunitFormatter  --out'
}
FRAMEWORK = environ.get('FRAMEWORK', 'pytest')

def main():
    report = '/tmp/obid'
    config = get_config()
    client = Client(config.project)
    sha = Git.sha()

    try:
        sha = client.sha(sha)
        print()
        print(view(sha))
        print()
    except ClientException:
        pass

    args = sys.argv[1:]

    if len(args) == 0:
        print("usage: testyoke pytest args")
        exit(1)

    args = args + [XML_ARG[FRAMEWORK], report]
    subprocess.call(args)

    if path.isfile(report):
        with open(report, 'r') as f:
            report = f.read()
            client.post(report, sha=sha.sha)
    else: 
        print(f"'{report}' is not a file.")
