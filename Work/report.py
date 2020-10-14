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
            holding = {
                'name': name,
                'share': share,
                'price': price
            }
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                name = row[0]
                price = float(row[1])
                prices[name] = price
    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices("Data/prices.csv")

total_cost = 0.0
for p in portfolio:
    price = p["share"] * prices[p["name"]]
    total_cost = total_cost + price
print(total_cost)
