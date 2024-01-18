from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import scraper
import re

load_dotenv()
OpenAI.api_key = os.environ['OPENAI_API_KEY']
client = OpenAI()


def api_call(msg):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msg,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def get_generator(stress_dir, url):
    config = json.load(open(os.path.join(stress_dir, 'stress_gen_prompt.json')))
    # input specification
    input_spec_prompt = config['input_spec']
    input_spec = scraper.get_input_spec(url)
    # example input text
    input_text_prompt = config['input_text_prompt']
    input_text = scraper.get_input_output(url)[0]
    # example code
    Example_code_prompt = config["Example_code_prompt"]
    Example_code = open(os.path.join(stress_dir, 'example_code.cpp'), 'r').read()
    # final reminder
    final_reminder = config["final_reminder"]
    prompt_text = input_spec_prompt + input_spec + input_text_prompt + input_text + Example_code_prompt + Example_code + final_reminder
    prompt = [{"role": "user", "content": prompt_text}]

    response = api_call(prompt)
    code = re.search("```([\s\S]*?)```", response).group(1)
    # check if the code is taking in input or printing
    match = re.search("cin", code)
    if match:
        print("cin found")
        prompt.append({"role": "assistant", "content": response})
        final_final_reminder = config["final_final_reminder"]
        prompt.append({"role": "user", "content": final_final_reminder})
        response = api_call(prompt)
        code = re.search("```([\s\S]*?)```", response).group(1)
    else:
        print("ai got it correct on first try!")
    print(code)
    return code


def get_brute_force(url):
    config = json.load(open("brute_force_prompt.json"))
