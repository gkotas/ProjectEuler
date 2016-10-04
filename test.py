from importlib import import_module
from os import listdir, path, remove
import sys
import argparse

# Dictionary showing the real answers for the problems
answers = {
    "pe001": 233168,
    "pe002": 4613732,
    "pe003": 6857,
    "pe004": 906609,
    "pe005": 232792560,
    "pe006": 25164150,
    "pe007": 104743,
    "pe008": 23514624000,
    "pe009": 31875000,
    "pe010": 142913828922,
    "pe011": 70600674,
    "pe012": 76576500,
    "pe013": 5537376230,
    "pe014": 837799,
    "pe015": 137846528820,
    "pe016": 1366,
    "pe017": 21124,
    "pe018": 1074,
    "pe019": 171,
    "pe020": 648,
    "pe021": 31626,
    "pe022": 871198282,
    "pe023": 4179871,
    "pe024": 278391560,
    "pe025": 4782,
    "pe026": 983,
    "pe027": -59231,
    "pe028": 669171001,
    "pe029": 9183,
    "pe030": 443839,
    "pe031": 73682,
    "pe032": 45228,
    "pe033": 100,
    "pe034": 40730,
    "pe035": 55,
    "pe036": 872187,
    "pe037": 748317,
    "pe038": 932718654,

}

def main(args):
    """
    Tests all or one problem, then cleans up.
    """
    if args.problem in answers:
        testProblem(args.problem)
    else:
        if args.problem != "":
            print "%s isn't a valid problem id." % args.problem
        else:
            for problem in answers.keys():
                testProblem(problem)

    cleanup_pyc()

def testProblem(problem):
    """
    Tests the problem specified and reports if it passes or not.
    """
    print "Testing problem %s..." % problem[2:],
    module = import_module(problem)
    if module.answer() == answers[problem]:
        print ""
    else:
        print "Failed!"

def cleanup_pyc():
    """
    Deletes all .pyc files when done testing.
    """
    dir_path = path.dirname(path.realpath(__file__))

    if sys.platform[:3] == "win":
        slash = "\\"
    else:
        slash = "/"

    for filename in listdir(dir_path):
        if filename.endswith(".pyc"):
            remove("%s%s%s" % (dir_path, slash, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run through all the problems to make sure they still work."
    )
    parser.add_argument(
        "--problem",
        help="Specify which one problem to test.",
        default=""
    )
    main(parser.parse_args())
