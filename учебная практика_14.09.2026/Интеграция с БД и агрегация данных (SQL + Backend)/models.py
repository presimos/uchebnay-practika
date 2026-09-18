from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Partner:
    partner_id: int
    company_name: str
    contact_email: str
    phone: str | None
    rating: Decimal | None
    total_quantity: int
    discount: int
