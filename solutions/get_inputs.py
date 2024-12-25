import os
import sys

import requests

SESSION_COOKIE = '53616c7465645f5fac5fe4749acb9e8f7f38bdc063cc361bdd8a59d10d4af343cb45d54a231ea941677ccf654331a57591ac41f9e3f46860eef1af89f00ffd29'

URL = "https://adventofcode.com/2024/day/%s/input"
BASE_DIR = os.path.join(os.path.dirname(__file__), "../inputs")


def run():
    if len(sys.argv) != 2:
        raise Exception("Invalid args, supply day number")

    day = sys.argv[1]
    print("Retrieving inputs for day " + day)

    if is_cached(day):
        print("Found cached input at location " + get_day_file(day))
        return 0

    inputs = get_inputs_from_web(day)
    print("Retrieved inputs from web (%s lines)" % len(inputs.split('\n')))
    cache_location = cache_inputs(day, inputs)
    print("Wrote inputs to location " + cache_location)
    return 0


def read_inputs(day, strip=True):
    day_file = get_day_file(day)
    with open(day_file, 'r') as f:
        text = f.read()
        if strip:
            text = text.strip()
        return [i for i in text.split('\n')]


def is_cached(day):
    day_file = get_day_file(day)
    return os.path.exists(day_file)


def get_day_dir(day):
    return os.path.join(BASE_DIR, str(day))


def get_day_file(day):
    return os.path.join(get_day_dir(day), 'input.txt')


def get_inputs_from_web(day):
    headers = {'Cookie': 'session=%s' % SESSION_COOKIE,
               'User-Agent': 'github.com/mdowell12/advent-of-code-2024 by mattdowell12@gmail.com'}
    resp = requests.get(URL % day, headers=headers)
    resp.raise_for_status()
    return resp.text


def cache_inputs(day, inputs):
    if not os.path.exists(get_day_dir(day)):
        os.mkdir(get_day_dir(day))
    file = get_day_file(day)
    with open(file, 'w') as f:
        f.write(inputs)
    return file


if __name__ == "__main__":
    sys.exit(run())
