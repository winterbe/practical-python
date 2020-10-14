# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # skip header
        for row in rows:
            name = row[0]
            share = int(row[1])
            price = float(row[2])
            holding = (name, share, price)
            portfolio.append(holding)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
