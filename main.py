# set up to link to python interpreter

import sys


def check_number_of_arguments(expect, args):
    if len(args) != expect:
        print("expected " + str(expect) + "arguments but got " + str(len(args)))
        sys.exit()


if len(sys.argv) < 2:
    print("invalid arguments")
    print("arguments are:")
    for arg in sys.argv:
        print(arg)
    sys.exit()

option = sys.argv[1]
match option:
    case "init":
        check_number_of_arguments(2, sys.argv)
        # todo call init function
    case "new":
        check_number_of_arguments(3, sys.argv)
        contest_url = sys.argv[2]
        # todo call new function
    case "refresh":
        check_number_of_arguments(2, sys.argv)
        # todo implement refresh logs
