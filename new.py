import os
import re
import requests
import json

import openai_utils
import scraper
import file_utils

def new_stress_dir(working_dir, skeleton_dir, dest_dir, url):
    config = json.load(open(os.path.join(working_dir, "config.json")))
    template_dir = os.path.join(skeleton_dir, config["language"])
    stress_dir = os.path.join(template_dir, "stress")
    stress_dest_dir = os.path.join(dest_dir, "stress")
    # copy entire stress testing dir
    print("copying stress testing dir")
    file_utils.copy_dir(stress_dir, stress_dest_dir)
    # get ai generated stress gen code
    code = openai_utils.get_generator(stress_dir, url)
    stress_gen_dest_dir = os.path.join(dest_dir, "stress", "Dgen.cpp")
    with open(stress_gen_dest_dir, "w") as file:
        file.write(code)


def new_problem(url, working_dir, dest_dir):
    skeleton_dir = os.path.join(working_dir, "skeleton")
    config = json.load(open(os.path.join(working_dir, "config.json")))
    template_path = os.path.join(skeleton_dir, config["language"], config[config["language"]]["template_name"])
    # web scrape to get name of problem
    title = scraper.get_problem_title(url)
    new_problem_path = os.path.join(dest_dir, title)
    # create problem dir
    file_utils.make_dirs(new_problem_path)
    # copy template code into directory
    file_utils.copy_file(template_path, os.path.join(new_problem_path, config[config["language"]]["solution file name"]))

    # create the example input.txt and output.txt
    tests_data = scraper.get_input_output(url)
    testcases_path = os.path.join(new_problem_path, "testcases")
    scraper.write_input_output(tests_data, testcases_path)

    # create stress test
    print("creating new stress_dir")
    new_stress_dir(working_dir, skeleton_dir, new_problem_path, url)


def new_contest(url, working_dir, dest_dir):
    # get contest id from url
    match = re.search(r"contest/(\d+)", url)
    contest_id = ""
    print(match)
    if match:
        contest_id = match.group(1)
    else:
        print("invalid url: cannot find contest ID in the link given")
        return

    # get contest info
    data = scraper.get_contest_info(url)
    contestName = data["contest_name"]

    new_contest_path = os.path.join(dest_dir, contestName)
    os.mkdir(new_contest_path)
    # call new_problem with each of the individual problem url
    problems = data["problems"]
    for problem in problems:
        problem_url = url + "/problem/" + problem["index"]
        new_problem(problem_url, working_dir, new_contest_path)


def new(url, working_dir, dest_dir):
    # check if the url is a contest or problem
    url_is_contest = not re.search("problem", url)

    # check if directory is contest dir
    dest_dir_name = re.search(r'[^/]*$', dest_dir)
    dir_is_contest = bool(re.search("contest", dest_dir_name.group(0).lower()))

    # warn user if there is a mismatch
    if url_is_contest != dir_is_contest:
        proceed = input(
            f"warning: would you like to create a new {'contest' if url_is_contest else 'problem'} in a {'contest' if dir_is_contest else 'problem'} directory? [y/n]").lower()
        if proceed == 'n':
            return
        elif proceed != 'y':
            print("invalid input: please respond with 'y' or 'n' without quotation marks")
            new(url, working_dir, dest_dir)

    if url_is_contest:
        new_contest(url, working_dir, dest_dir)
    else:
        new_problem(url, working_dir, dest_dir)
