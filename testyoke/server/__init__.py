import json
from flask import Flask, request, Response
from testyoke.formats.xml import junit
from xml.etree.ElementTree import ParseError

from testyoke import api

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

def params():
    return {
        'flaky': request.args.get('flaky') is not None
    }


@app.route('/projects/<string:project>/reports', methods=['POST'])
def receive_report(project):
    sha = request.headers.get('vc-sha', '').strip()

    try:
        suites = get_parser(
            request.headers['content-type']
        ).parse(request.get_data(), sha=sha)
    except ParseError:
        return '{"message": "report not parsable"}', 400

    api.receive_report(suites, project, sha)

    return "", 201


@app.route('/projects/<string:project>')
def stats_project(project):
    return Response(json.dumps(api.get_stats(project, **params())), headers=headers())


@app.route('/projects/<string:project>/<string:suite>')
def stats_suite(project, suite):
    case = api.get_stats(project, **params()).get(suite)
    return Response(json.dumps(case), headers=headers())


@app.route('/projects/<string:project>/<string:suite>/<string:test>')
def stats_test(project, suite, test):
    case = api.get_stats(project, **params()).get(suite).get(test)
    return Response(json.dumps(case), headers=headers())

#
# VC SHAS
#

@app.route('/projects/<string:project>/shas') 
def get_shas(project):
    """ missing project """
    return Response(json.dumps(api.get_shas(project)), headers=headers())


@app.route('/projects/<string:project>/shas/<string:sha>') 
def get_sha(project, sha):
    """ missing project """
    sha = api.get_sha(project, sha)

    # TODO GARBAGE
    response = sha.to_dict if sha is not None else {'message': 'Not Found'}
    return Response(json.dumps(response), headers=headers())

#
# welcome
#

@app.route('/')
def welcome():
    return 'testharness <a href="/projects/aproj/stats">aproj</a>'

