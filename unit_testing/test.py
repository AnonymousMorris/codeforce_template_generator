import shutil

import new
import init
import os
import json

def check_file_structure(path, testing_dir):
    file_struct = None
    file_struct = json.load(open(testing_dir))


if __name__ == '__main__':
    testing_space_dir = os.path.join(os.getcwd(), "testing_space")
    program_dir = "/home/ghost2/PycharmProjects/cf gen"
    os.mkdir(testing_space_dir)
    print(testing_space_dir)
    print(program_dir)
    init.init(testing_space_dir, program_dir)
    url = "https://codeforces.com/contest/1919"
    new.new(url, testing_space_dir, os.path.join(testing_space_dir, "contests"))

    clean = input("rm -r testing_space? [y/n]")
    if clean.lower == 'y':
        shutil.rmtree(testing_space_dir)
