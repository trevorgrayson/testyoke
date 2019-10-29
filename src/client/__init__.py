import json
from http.client import HTTPConnection
from models import ProjectState

class ClientException(Exception): pass

class Client:

    def __init__(self, project, hostname='localhost', port=7357):
        self.conn = HTTPConnection(hostname, port)
        self.project = project

    def sha(self, sha):
        self.conn.request("GET", "/projects/%s/shas/%s" % (self.project, sha))
        res = self.conn.getresponse()

        
        if res.status == 200:
            data = json.loads(res.read())
            return ProjectState(**data)
        else:
            raise ClientException("%s: %s" % (res.status, res.reason))
        
    # def case(self, case):
    # def report(self):
        

