from flask import Flask, request, Response
import json
import api
from formats.xml import junit

app = Flask(__name__)

CONTENT_TYPES = {
    'application/xml+junit': junit
}

def get_parser(content_type):
    return CONTENT_TYPES.get(content_type, junit)

def headers():
    return {
        "Content-Type": "application/json"
    }

@app.route('/projects/<string:project>/reports', methods=['POST'])
def receive_report(project):
    suites = get_parser(request.headers['content-type']).parse(request.get_data())
    sha = request.headers.get('vc-sha').strip()

    api.receive_report(suites, project, sha)

    return "", 201


@app.route('/projects/<string:project>')
def stats_project(project):
    return Response(json.dumps(api.get_stats(project)), headers=headers())


@app.route('/projects/<string:project>/<string:suite>/<string:test>')
def stats_test(project, suite, test):
    case = api.get_stats(project).get(suite).get(test)
    return Response(json.dumps(case), headers=headers())


@app.route('/')
def welcome():
    return 'testharness <a href="/projects/aproj/stats">aproj</a>'
