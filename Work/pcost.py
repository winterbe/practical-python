# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    f = open(filename, "rt")
    try:
        next(f)
        cost = 0.0
        for line in f:
            try:
                row = line.split(",")
                share = int(row[1])
                price = float(row[2])
                cost = cost + (share * price)
            except ValueError:
                print("Could not handle row:", line, end="")
        return cost
    finally:
        f.close()


print(portfolio_cost("Data/portfolio.csv"))
print(portfolio_cost("Data/missing.csv"))
