from optparse import OptionParser
from os import environ, path
from glob import glob
from testyoke.config import TESTYOKE_PROD
from testyoke import stat
from testyoke.client import ClientException

from . import Client


def post_report(report, sha):
    if path.isfile(report):
        with open(report, 'r') as f:
            report = f.read()
            client.post(report, sha=sha)
    else: 
        print(f"'{report}' is not a file.")

            
if __name__ == '__main__':
    parser = OptionParser()

    vcsha = stat.vcsha()
    project_name = stat.project_name()

    parser.add_option("-s", "--sha", dest="sha", default=vcsha,
                  help="retrieve or report for provided version control sha", metavar=vcsha)
    parser.add_option("-p", "--project", dest="project", default=project_name,
                  help="name for this project", metavar=project_name)
    parser.add_option("-P", "--port", dest="port", default=7357,
                  help="port of host server", metavar="7357")
    parser.add_option("-H", "--host", dest="host", default=TESTYOKE_PROD,
                  help="hostname of server")
    parser.add_option("-r", "--report", dest="report",
                  help="test report file to submit (Unix globbing*)", metavar="JUNIT.xml")

    opts, args = parser.parse_args()

    if not opts.project or (not opts.sha and not opts.report):
        parser.print_help()
        exit(0)

    port = opts.port
    if opts.host == TESTYOKE_PROD:
        port = 80

    client = Client(opts.project, hostname=opts.host, port=port)

    if opts.sha and not opts.report:  # should this return after report uploaded?
        try:
            sha = client.sha(opts.sha)

            print()
            print("########################################################")
            print(f"# sha: {sha.sha.ljust(47)} #")
            print(f"# {repr(sha).ljust(53)}#")
            print("#                                                      #")
            print("########################################################")
            print()
        except ClientException as err:
            print("There was a problem retrieving the {} project. {}".format(opts.project, err))
            parser.print_help()
            exit(0)


    if opts.report:
        print(f"matching: {opts.report}", end=" ")
        for report_file in glob(opts.report):
            post_report(report_file, opts.sha)
            print('', end=".")

        print('done.')
