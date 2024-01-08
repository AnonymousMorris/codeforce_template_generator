import os
import sys
import file_utlls

print(sys.path)
print(os.getcwd())
working_dir = os.getcwd()
program_path = os.path.dirname(os.path.realpath(__file__))


def init():
    file_utlls.notify_working_and_program_path()
    if file_utlls.is_cf_dir():
        print(working_dir + " is already a contest space")
        sys.exit()
    else:
        contests_dir = os.path.join(working_dir, "contests")
        os.mkdir(contests_dir)
        practice_dir = os.path.join(working_dir, "practice_problems")
        os.mkdir(practice_dir)
        skeleton_dest_path = os.path.join(working_dir, "skeleton")
        skeleton_src_path = os.path.join(program_path, "skeleton")
        file_utlls.copy_dir(skeleton_src_path, skeleton_dest_path)
        config_dest_path = os.path.join(working_dir, "config.json")
        config_src_path = os.path.join(program_path, "config.json")
        file_utlls.copy_file(config_src_path, config_dest_path)
        print("successfully created contest space")


if __name__ == "__main__":
    init()
