from collections.abc import Sequence
from decimal import Decimal


PARTNERS_WITH_TOTALS_QUERY = """
SELECT
    p.partner_id,
    p.company_name,
    p.contact_email,
    p.phone,
    p.rating,
    COALESCE(SUM(sh.quantity), 0)::INTEGER AS total_quantity
FROM partners AS p
LEFT JOIN sales_history AS sh
    ON sh.partner_id = p.partner_id
GROUP BY
    p.partner_id,
    p.company_name,
    p.contact_email,
    p.phone,
    p.rating
ORDER BY p.company_name;
"""


class PartnerRepository:
    def __init__(self, connection: object) -> None:
        self._connection = connection

    def fetch_partners_with_totals(
        self,
    ) -> Sequence[tuple[int, str, str, str | None, Decimal | None, int]]:
        with self._connection.cursor() as cursor:
            cursor.execute(PARTNERS_WITH_TOTALS_QUERY)
            return cursor.fetchall()
