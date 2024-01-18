import sys
import os
import shutil


def is_cf_dir(path):
    print("is_cf_dir called with path " + path)
    return os.path.exists(os.path.join(path, "config.json"))


def check_path_exists(file_path):
    exists = os.path.exists(file_path)
    if exists:
        print("warning: " + file_path + " already exists")
        option = input("Would you like to overwrite the file? [y/n]")
        option = option.lower()
        if option == "y":
            os.remove(file_path)
        elif option == "n":
            sys.exit()
        else:
            print("invalid input: please enter [y/n]")
            check_path_exists(file_path)
    return exists


def copy_file(src_path, dest_path):
    check_path_exists(dest_path)
    print("copying " + src_path + " to " + dest_path)
    shutil.copy(src_path, dest_path)


def copy_dir(src_path, dest_path):
    if check_path_exists(dest_path):
        print("copy dir called with args:" + src_path + " to " + dest_path)
    shutil.copytree(src_path, dest_path)


def make_dirs(path):
    check_path_exists(path)
    os.mkdir(path)