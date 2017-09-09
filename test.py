from importlib import import_module
from os import listdir, path, remove, walk
from time import time
import sys
import argparse

# List showing the real answers for the problems
answers = [
    ("pe001", 233168),
    ("pe002", 4613732),
    ("pe003", 6857),
    ("pe004", 906609),
    ("pe005", 232792560),
    ("pe006", 25164150),
    ("pe007", 104743),
    ("pe008", 23514624000),
    ("pe009", 31875000),
    ("pe010", 142913828922),
    ("pe011", 70600674),
    ("pe012", 76576500),
    ("pe013", 5537376230),
    ("pe014", 837799),
    ("pe015", 137846528820),
    ("pe016", 1366),
    ("pe017", 21124),
    ("pe018", 1074),
    ("pe019", 171),
    ("pe020", 648),
    ("pe021", 31626),
    ("pe022", 871198282),
    ("pe023", 4179871),
    ("pe024", 278391560),
    ("pe025", 4782),
    ("pe026", 983),
    ("pe027", -59231),
    ("pe028", 669171001),
    ("pe029", 9183),
    ("pe030", 443839),
    ("pe031", 73682),
    ("pe032", 45228),
    ("pe033", 100),
    ("pe034", 40730),
    ("pe035", 55),
    ("pe036", 872187),
    ("pe037", 748317),
    ("pe038", 932718654),
    ("pe039", 840),
    ("pe040", 210),
    ("pe041", 7652413),
    ("pe042", 162),
    ("pe043", 16695334890),
    ("pe044", 5482660),
    ("pe045", 1533776805),
    ("pe053", 4075),
    ("pe054", 376),
    ("pe055", 249),
    ("pe056", 972),
    ("pe057", 153),
    ("pe058", 26241),
    ("pe059", 107359),
    ("pe060", 26033),
    ("pe061", 28684),
    ("pe062", 5027),
    ("pe063", 49),
    ("pe046", 5777),
    ("pe048", 9110846700),
    ("pe049", 296962999629),
    ("pe050", 997651),
]


def main():
    """
    Tests all problems, then cleans up.
    """
    for problem in answers:
        testProblem(problem)

    cleanup_pyc()


def testProblem(problem):
    """
    Tests the problem specified and reports if it passes or not.
    """
    module = import_module("problems." + problem[0])
    print "{}: Passed:".format(problem[0]),
    t0 = time()
    answer = module.answer()
    total_time = time() - t0

    if answer == problem[1]:
        print "True, Time: {:6.3f}".format(total_time),
        if total_time > 60:
            print "Too long"
        else:
            print ""
    else:
        print "False, Expected: {}, Got {}".format(problem[1], answer)


def cleanup_pyc():
    """
    Deletes all .pyc files when done testing.
    """
    dir_path = path.dirname(path.realpath(__file__))

    for root, dirs, files in walk(dir_path):
        for filename in files:
            if filename.endswith('.pyc'):
                remove(path.join(root, filename))


if __name__ == "__main__":
    main()
