from os import environ

from . import Client


project = 'testharness'
client = Client(project)

sha = environ.get('SHA')

if sha is not None:
    sha = client.sha(sha)
    print("###################################################")
    print("#")
    print(f"# {repr(sha)}")
    print("#")
    print("###################################################")
