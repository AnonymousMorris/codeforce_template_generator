from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import scraper

load_dotenv()
OpenAI.api_key = os.environ['OPENAI_API_KEY']
client = OpenAI()


def api_call(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(completion.choices[0].message.content)


def get_generator(url):
    config = json.load(open('prompt.json'))
    url = "https://codeforces.com/contest/1919/problem/C"
    # input specification
    input_spec_prompt = config['input_spec']
    input_spec = scrapper.get_input_spec(url)
    # example input text
    input_text_prompt = config['input_text_prompt']
    input_text = scrapper.get_input_text(url)
    # example code
    Example_code_prompt = config["Example_code_prompt"]
    Example_code = open('example_code.txt', 'r').read()
    # final reminder
    final_reminder = config["final_reminder"]
    prompt = input_spec_prompt + input_spec + input_text_prompt + input_text + Example_code_prompt + Example_code + final_reminder
    return api_call(prompt)