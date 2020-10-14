# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    f = open(filename, "rt")
    try:
        rows = csv.reader(f)
        next(rows)  # ignore headers
        cost = 0.0
        for row in rows:
            try:
                share = int(row[1])
                price = float(row[2])
                cost = cost + (share * price)
            except ValueError:
                print("Could not handle row:", row)
        return cost
    finally:
        f.close()


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
