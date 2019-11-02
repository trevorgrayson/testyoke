from optparse import OptionParser
from os import environ

from . import Client


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--sha", dest="sha",
                  help="retrieve report for provided sha", metavar="VC SHA")
    parser.add_option("-p", "--project", dest="project",
                  help="name for this project", metavar="PROJECT")
    parser.add_option("-r", "--report", dest="report",
                  help="test report file to submit", metavar="JUNIT.xml")

    opts, args = parser.parse_args()

    if not opts.project or (not opts.sha and not opts.report):
        parser.print_help()
        exit(0)

    client = Client(opts.project)

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
        print(f"sending {opts.report}")
        with open(opts.report, 'r') as f:
            report = f.read()
            client.post(report, sha=opts.sha)
            
