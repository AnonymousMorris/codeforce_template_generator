#!/bin/python3

import os
import sys

import init
import new
import file_utils

def check_number_of_arguments(expect, args):
    if len(args) != expect:
        print("expected " + str(expect) + " arguments but got " + str(len(args)))
        sys.exit()


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("invalid arguments")
    print("arguments are:")
    for arg in sys.argv:
        print(arg)
    sys.exit()

# store path to working directory and program directory
dest_dir = os.getcwd()
working_dir = os.getcwd()
# while not file_utils.is_cf_dir(working_dir):
#     working_dir = os.path.dirname(working_dir)
#     if working_dir == "/":
#         print("Error: cannot find codeforce space. Make sure to use cf init")
#         sys.exit()
program_path = os.path.dirname(os.path.realpath(__file__))

def check_path():
    print("working directory: " + working_dir)
    print("program path: " + program_path)
    print("destination directory: " + dest_dir)

# call method corresponding to arg
option = sys.argv[1]
print("option is " + option)
match option:
    case "init":
        print("doing init")
        check_number_of_arguments(2, sys.argv)
        init.init(dest_dir, program_path)
    case "new":
        check_number_of_arguments(3, sys.argv)
        contest_url = sys.argv[2]
        new.new(contest_url, working_dir, dest_dir)
    case "refresh":
        check_number_of_arguments(2, sys.argv)
        # todo implement refresh logs
