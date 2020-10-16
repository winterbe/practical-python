from random import random
from time import sleep


def generate_number():
    while True:
        sleep(0.5)
        yield random()


def filter_numbers(numbers):
    for n in numbers:
        if n > 0.5:
            yield n

# Generator expression variant:
# def filter_numbers(numbers):
#     return (x for x in numbers if x > 0.5)


n = generate_number()
f = filter_numbers(n)
for i, n in enumerate(f):
    if i > 10:
        break
    else:
        print(f"{i:>2}: {n}")
