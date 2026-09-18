from collections.abc import Sequence
from decimal import Decimal

from discount import calculate_partner_discount
from models import Partner


PartnerRow = tuple[int, str, str, str | None, Decimal | None, int]


def build_partners_with_discounts(rows: Sequence[PartnerRow]) -> list[Partner]:
    partners: list[Partner] = []
    for row in rows:
        partner_id, company_name, contact_email, phone, rating, total_quantity = row
        discount = calculate_partner_discount(total_quantity)
        partner = Partner(
            partner_id=partner_id,
            company_name=company_name,
            contact_email=contact_email,
            phone=phone,
            rating=rating,
            total_quantity=total_quantity,
            discount=discount,
        )
        partners.append(partner)
    return partners
