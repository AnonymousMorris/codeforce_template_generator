# set up to link to python interpreter

import requests
import sys
import re
from scraper import get_input_output

if len(sys.argv) != 2:
    print("wrong number of arguments")
    sys.exit()

contest_url = sys.argv[1]
match = re.search(r"(\d+)$", contest_url)

contestID = ""
print(match)
if match:
    contestID = match.group(1)
else:
    print("invalid input: cannot find contest ID in the link given")
    sys.exit()

print(contestID)

apiURL = ("https://codeforces.com/api/contest.standings?contestId={"
          "contestId}&asManager=false&from=1&count=5&showUnofficial=true")
contestURL = apiURL.format(contestId=str(contestID))
response = requests.get(contestURL)

# confirms success of api call else quit
if not response.ok:
    print("api call failed: try waiting 2 seconds before retrying")
    sys.exit()

data = response.json()
contestName = data["result"]["contest"]["name"]
problems = data["result"]["problems"]
problem_names = []
for problem in problems:
    problem_names.append(problem["index"] + ": " + problem["name"])

# getting input and output text of all problems in contest
input_output_text = []
for problem in problems:
    url = contestURL + "problem/{index}"
    url.format(index=problem["index"])
    input_output_text.append(get_input_output(url))