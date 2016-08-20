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
