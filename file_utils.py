import sys
import os
import shutil

working_dir = os.getcwd()
program_path = os.path.dirname(os.path.realpath(__file__))


def notify_working_and_program_path():
    print("Notifying working directory")
    print(working_dir)
    print(program_path)


def is_cf_dir(path):
    notify_working_and_program_path()
    return os.path.exists(os.path.join(path, "config.json"))


def check_path_exists(file_path):
    exists = os.path.exists(file_path)
    if exists:
        print("warning: " + file_path + " already exists")
        print("Would you like to overwrite the file? y/n")
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
    shutil.copy(src_path, dest_path)


def copy_dir(src_path, dest_path):
    check_path_exists(dest_path)
    shutil.copytree(src_path, dest_path)


if __name__ == "__main__":
    notify_working_and_program_path()
    print(is_cf_dir(working_dir))
