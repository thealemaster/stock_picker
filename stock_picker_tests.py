import unittest

from stock_picker import calculate_profit

class TestProfitCalculation (unittest.TestCase):
    def test_max_val_as_first_price_returns_zero(self):
        price_list = [5, 4, 3, 2, 1]
        result = calculate_profit (price_list)
        self.assertEqual (result, 0)

    def test_max_val_as_second_price_returns_second_value_minus_first_value(self):
        price_list = [4, 5, 3, 2, 1]
        result = calculate_profit (price_list)
        self.assertEqual (result, 1)
        

if __name__ == '__main__':
    unittest.main()

