import unittest
from decimal import Decimal

from service import build_partners_with_discounts


class PartnerServiceTests(unittest.TestCase):
    def test_partner_without_sales_has_zero_discount(self) -> None:
        rows = [(4, "ООО Новый партнёр", "new@example.ru", None, Decimal("5.0"), 0)]
        partners = build_partners_with_discounts(rows)
        self.assertEqual(partners[0].total_quantity, 0)
        self.assertEqual(partners[0].discount, 0)
