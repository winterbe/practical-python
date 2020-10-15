# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None, has_headers=True, silence_errors=True, delimiter=','):
    """
    Parse a CSV file into a list of records
    """
    if not has_headers and select:
        raise RuntimeError("wrong combination of args")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            headers = None

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for index, row in enumerate(rows):
            try:
                if not row:  # Skip rows with no data
                    continue

                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]

                if types:
                    row = [func(val) for func, val in zip(types, row)]

                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)

                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {index + 1}: Couldn't convert", row)
                    print(f"Row {index + 1}: Reason", e)
                pass

    return records


# def test():
#     portfolio = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=False)
#     pprint(portfolio)
#
#
# test()
