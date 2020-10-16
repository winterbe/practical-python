from unittest import TestCase

from Work.stock import Stock


class TestStock(TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock("a", 100, 10.0)
        self.assertEqual(s.cost, 1000)

    def test_sell(self):
        s = Stock("a", 100, 10.0)
        s.sell(100)
        self.assertEqual(s.shares, 0)
