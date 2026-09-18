import sys
from decimal import Decimal
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
TASK_1_DIR = PROJECT_DIR / "Разработка ядра бизнес-логики (Расчет скидки)"
TASK_2_DIR = PROJECT_DIR / "Интеграция с БД и агрегация данных (SQL + Backend)"
TASK_3_DIR = PROJECT_DIR / "Разработка интерфейса (UI) по руководству по стилю"

for task_dir in (TASK_1_DIR, TASK_2_DIR, TASK_3_DIR):
    sys.path.insert(0, str(task_dir))

from discount import calculate_partner_discount
from models import Partner
from ui import PartnerCrmApp


def create_demo_partner(
    partner_id: int,
    company_name: str,
    total_quantity: int,
) -> Partner:
    return Partner(
        partner_id=partner_id,
        company_name=company_name,
        contact_email=f"partner{partner_id}@example.ru",
        phone="+79990000000",
        rating=Decimal("5.0"),
        total_quantity=total_quantity,
        discount=calculate_partner_discount(total_quantity),
    )


def main() -> None:
    partners = [
        create_demo_partner(1, "ООО Демонстрация без скидки", 9999),
        create_demo_partner(2, "ООО Демонстрация базовой скидки", 10000),
        create_demo_partner(3, "ООО Демонстрация максимальной скидки", 300000),
    ]
    resources_dir = TASK_3_DIR / "resources"
    application = PartnerCrmApp(partners, resources_dir)
    application.mainloop()


if __name__ == "__main__":
    main()
