# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = row[0]
            share = int(row[1])
            price = float(row[2])
            holding = dict(zip(headers, (name, share, price)))
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


def make_report(portfolio, prices):
    rows = []
    for p in portfolio:
        name = p["name"]
        share = p["shares"]
        price = p["price"]
        current_price = prices[name]
        change = current_price - price
        rows.append((name, share, current_price, change))
    return rows


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    line = '-' * 10
    print('%10s %10s %10s %10s' % (line, line, line, line))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
