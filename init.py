import sys
import os
import shutil

print(sys.path)
print(os.getcwd())
working_dir = os.getcwd()
absolute_path = os.path.dirname(os.path.realpath(__file__))


def is_cf_dir():
    return os.path.exists(os.path.join(working_dir, ".config.json"))


def check_file_exists(file_path):
    exists = os.path.exists(file_path)
    if exists:
        print("warning: " + file_path + " already exists")
        print("Would you like to overwrite the file? y/n")
        option = input("Would you like to overwrite the file? [y/n]")
        option = option.lower()
        if option == "y":
            os.remove(file_path)
        else:
            sys.exit()
    return exists


if is_cf_dir:
    print(working_dir + " is already a contest space")
    sys.exit()
else:
    contests_dir = os.path.join(working_dir, "contests")
    os.mkdir(contests_dir)
    practice_dir = os.path.join(working_dir, "practice")
    os.mkdir(practice_dir)


def copy_file(src_path, dest_path):
    check_file_exists(dest_path)
    shutil.copy(src_path, dest_path)

