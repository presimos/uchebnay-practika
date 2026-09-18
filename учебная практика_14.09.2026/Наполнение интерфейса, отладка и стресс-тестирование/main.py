import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
TASK_1_DIR = PROJECT_DIR / "Разработка ядра бизнес-логики (Расчет скидки)"
TASK_2_DIR = PROJECT_DIR / "Интеграция с БД и агрегация данных (SQL + Backend)"
TASK_3_DIR = PROJECT_DIR / "Разработка интерфейса (UI) по руководству по стилю"

for task_dir in (TASK_1_DIR, TASK_2_DIR, TASK_3_DIR):
    sys.path.insert(0, str(task_dir))

from database import open_connection
from repository import PartnerRepository
from service import build_partners_with_discounts
from ui import PartnerCrmApp


def main() -> None:
    resources_dir = TASK_3_DIR / "resources"
    with open_connection() as connection:
        repository = PartnerRepository(connection)
        rows = repository.fetch_partners_with_totals()
    partners = build_partners_with_discounts(rows)
    application = PartnerCrmApp(partners, resources_dir)
    application.mainloop()


if __name__ == "__main__":
    main()
