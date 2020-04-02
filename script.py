import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://bjex.ca")
print(greet("World"))
print(greet("Bing"))
print(r.status_code)
