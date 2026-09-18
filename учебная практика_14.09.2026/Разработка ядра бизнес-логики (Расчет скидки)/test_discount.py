import unittest

from discount import calculate_partner_discount


class CalculatePartnerDiscountTests(unittest.TestCase):
    def test_returns_zero_below_first_threshold(self) -> None:
        self.assertEqual(calculate_partner_discount(9999), 0)

    def test_returns_five_at_first_threshold(self) -> None:
        self.assertEqual(calculate_partner_discount(10000), 5)

    def test_returns_five_at_second_threshold_minus_one(self) -> None:
        self.assertEqual(calculate_partner_discount(49999), 5)

    def test_returns_ten_at_second_threshold(self) -> None:
        self.assertEqual(calculate_partner_discount(50000), 10)

    def test_returns_fifteen_at_last_threshold(self) -> None:
        self.assertEqual(calculate_partner_discount(300000), 15)
