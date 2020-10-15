from Work.fileparse import parse_csv


class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, amount: int):
        self.shares = max(self.shares - amount, 0)


def test():
    with open("Data/portfolio.csv", "rt") as lines:
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio = [Stock(p["name"], p["shares"], p["price"]) for p in portdicts]
        print(sum([s.cost() for s in portfolio]))

