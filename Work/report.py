#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

from Work.fileparse import parse_csv
from Work.stock import Stock


def read_portfolio(filename):
    with open(filename, "rt") as f:
        dicts = parse_csv(f, types=[str, int, float])
        return [Stock(p["name"], p["shares"], p["price"]) for p in dicts]


def read_prices(filename):
    with open(filename, "rt") as f:
        prices = parse_csv(f, types=[str, float], has_headers=False, silence_errors=True)
        return dict(prices)


def make_report(portfolio, prices):
    rows = []
    for p in portfolio:
        name = p.name
        shares = p.shares
        price = p.price
        current_price = prices[name]
        change = current_price - price
        rows.append((name, shares, current_price, change))
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


def main(argv):
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    # portfolio_report(argv[0], argv[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)
