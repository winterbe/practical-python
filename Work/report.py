#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from pprint import pprint

from Work import tableformat
from Work.fileparse import parse_csv
from Work.stock import Stock


def read_portfolio(filename):
    with open(filename, "rt") as f:
        dicts = parse_csv(f, types=[str, int, float])
        return [Stock(**p) for p in dicts]


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


def print_report(reportdata, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    portfolio = read_portfolio('Data/portfolio.csv')
    portfolio.sort(key=lambda s: s.shares)
    pprint(portfolio)

    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    # portfolio_report(argv[0], argv[1])


if __name__ == '__main__':
    import sys

    main(sys.argv)
