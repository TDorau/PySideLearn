import math
import sys
from os import rename

import requests

name = input("Your name? ")
print("Hello", name)

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('World'))
print(greet('Corey'))
