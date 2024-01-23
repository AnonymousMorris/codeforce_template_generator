import os

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
    print("URL request is" + url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    example = soup.find("div", {"class": "sample-test"})

    inputs = example.find_all("div", {"class" : "input"})
    input_texts = []
    for inp in inputs:
        inp_text = ""
        for line in inp.find_all("div", {"class" : "test-example-line"}):
            inp_text += (line.text + "\n")
        input_texts.append(inp_text)
        print("Input")
        print(inp_text)

    outputs = example.find_all("div", {"class" : "output"})
    output_texts = []
    for out in outputs:
        out_text = out.find("pre").text
        output_texts.append(out_text)
        print("Output")
        print(out_text)

    ans = [input_texts, output_texts]
    return ans

def write_input_output(input_output_texts, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for idx, text in enumerate(input_output_texts[0]):
        file = open(os.path.join(output_path, "in" + str(idx)), "w")
        file.write(text)
        file.close()

    for idx, text in enumerate(input_output_texts[1]):
        file = open(os.path.join(output_path, "cor" + str(idx)), "w")
        file.write(text)
        file.close()

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
