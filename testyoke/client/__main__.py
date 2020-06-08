from optparse import OptionParser
from os import environ, path
from glob import glob

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
    parser.add_option("-s", "--sha", dest="sha",
                  help="retrieve report for provided sha", metavar="VC SHA")
    parser.add_option("-p", "--project", dest="project",
                  help="name for this project", metavar="PROJECT")
    parser.add_option("-r", "--report", dest="report",
                  help="test report file to submit (Unix globbing*)", metavar="JUNIT.xml")
    parser.add_option("-h", "--host", dest="host",
                  help="hostname", default="testyoke.com")
    parser.add_option("-P", "--port", dest="port", type="int",
                  help="port", default=80)

    opts, args = parser.parse_args()

    if not opts.project or (not opts.sha and not opts.report):
        parser.print_help()
        exit(0)

    client = Client(opts.project, 
                    hostname=opts.host, 
                    port=opts.port)

    if opts.sha and not opts.report:  # should this return after report uploaded?
        sha = client.sha(opts.sha)

        print()
        print("########################################################")
        print(f"# sha: {sha.sha.ljust(47)} #")
        print(f"# {repr(sha).ljust(53)}#")
        print("#                                                      #")
        print("########################################################")
        print()


    if opts.report:
        print(f"matching: {opts.report}", end=" ")
        for report_file in glob(opts.report):
            post_report(report_file, opts.sha)
            print('', end=".")

        print('done.')
