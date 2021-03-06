from Work.typedproperty import StringProp, IntProp, FloatProp


class Stock:
    name = StringProp('name')
    shares = IntProp('shares')
    price = FloatProp('price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, amount: int):
        self.shares = max(self.shares - amount, 0)

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"


def main():
    s = Stock("bla", 100, 9.9)
    print(s)
    with open("Data/portfolio.csv", "rt") as lines:
        from Work.fileparse import parse_csv
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio = [Stock(p["name"], p["shares"], p["price"]) for p in portdicts]
        print(sum([s.cost for s in portfolio]))


if __name__ == "__main__":
    main()
