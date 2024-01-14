import openai_utils


def create_stress_gen(url):
    code = openai_utils.get_generator(url)


def create_brute_force(url):
    code = openai_utils.get_brute_force(url)
