#
# EXPERIMENTAL
#
# functional passing of cases and suites
# outputs insights
#
# if it takes more than one pass to label a test, that's
# ok, because they are the same test.
#
# `persist` needs to eventually have some snapshot of tests
#
# does this work?
#
# result_stream -> analytics_mark_up -> save, snapshot
#
# can get stream of cases from service or persist
# TODO need to pull stuff out of persist.file
#
#
# Need CQRS pattern. can warm up from disk, or not,
# depends on the analysis' needs.
# expect this dir to break down into parts
# TESTS
#

AGGREGATE = {} # by test_id


def analyze_test(case, suite, **options):
    """ 
    pass test cases through to mark up analytical data

    case - 
    suite -
    environ - ?
    **options
    """

    mark_flaky(case, suite, **options)
    mark_regressive(case, suite, **options)

    # if all_tests_pass: 
    #    save(sha, passed_shas)
    # else:
    # defect-shas


def mark_flaky(case, suite, **options):
    """ 
    flaky - passes and fails on same SHA.
    check if is_flaky, mark test 
    """
    if False:
        case.is_flaky = True


def mark_regressive(case, suite, **options):
    """
    regression - fails, is fixed, fails on new commit. not flaky.
    b
    """
    if False:
        case.is_regressive = True


def mark(case, cases, fn):
    """ takes test case, and it's relatives, and a lambda to make a decision """
