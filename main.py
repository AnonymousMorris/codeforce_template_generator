# set up to link to python interpreter
import os
import sys

import init
import new
import file_utils


def check_number_of_arguments(expect, args):
    if len(args) != expect:
        print("expected " + str(expect) + "arguments but got " + str(len(args)))
        sys.exit()


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("invalid arguments")
    print("arguments are:")
    for arg in sys.argv:
        print(arg)
    sys.exit()

option = sys.argv[1]

# store path to working directory and program directory
dest_dir = os.getcwd()
working_dir = os.getcwd()
while not file_utils.is_cf_dir(working_dir):
    working_dir = os.path.dirname(working_dir)
    if working_dir == "/":
        print("Error: cannot find codeforce space. Make sure to use cf init")
        sys.exit()
program_path = os.path.dirname(os.path.realpath(__file__))

match option:
    case "init":
        check_number_of_arguments(2, sys.argv)
        init.init(working_dir, program_path)
    case "new":
        check_number_of_arguments(3, sys.argv)
        contest_url = sys.argv[2]
        new.new(contest_url, working_dir, dest_dir)
    case "refresh":
        check_number_of_arguments(2, sys.argv)
        # todo implement refresh logs
