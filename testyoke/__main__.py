#!/usr/bin/env python
#
# usage:
#       testyoke pytest 
#       testyoke rspec
#
# automatically add appropriate parameter, grab file
#
import sys
from os import environ, path, getcwd
import argparse
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

report = '/tmp/obid'
project = 'testyoke'

if __name__ == '__main__':
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
    args = args + [XML_ARG['pytest'], report]
    subprocess.call(args)

    if path.isfile(report):
        with open(report, 'r') as f:
            report = f.read()
            client.post(report, sha=sha.sha)
    else: 
        print(f"'{report}' is not a file.")
