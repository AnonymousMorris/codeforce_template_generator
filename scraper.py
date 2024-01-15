import itertools

import requests
from bs4 import BeautifulSoup


def get_contest_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # getting the title of the contest
    title_box = soup.find("table", {"class": "rtable"})
    title = title_box.find("a").get_text()
    # getting the indexes of the problems
    problems_table = soup.find("table", {"class": "problems"})
    problems_rows = problems_table.find_all("tr")
    problems = []
    for i, row in enumerate(problems_rows):
        if i == 0:
            continue
        else:
            problem = [data.find("a").get_text(strip=True) for data in itertools.islice(row.find_all("td"), 2)]
            problems.append({"index": problem[0], "name": problem[1]})
    print("contest: " + title + "\nproblems: ", end="")
    print(problems)
    return {"contest_name": title, "problems": problems}


def get_input_output(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    Example = soup.find("div", {"class": "sample-test"})
    raw_input_text = Example.find_all("div", {"class": "test-example-line"})
    input_text = ""
    for line in raw_input_text:
        input_text += (line.text + "\n")
    print(input_text)
    output = Example.find("div", {"class": "output"})
    output_text = output.text
    print(output_text)
    ans = [input_text, output_text]
    return ans


def get_problem_title(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.select_one('.header .title').text
    return title


def get_input_spec(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    Input_spec = soup.find("div", {"class": "input-specification"})
    return Input_spec.text
