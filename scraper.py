import requests
from bs4 import BeautifulSoup


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
