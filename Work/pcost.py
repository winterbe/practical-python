# pcost.py
#
# Exercise 1.27

import sys
from Work.fileparse import parse_csv


def portfolio_cost(filename):
    return parse_csv(filename, select=["shares", "price"], types=[int, float], silence_errors=True)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
