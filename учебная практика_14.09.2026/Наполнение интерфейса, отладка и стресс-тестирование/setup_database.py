import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
TASK_2_DIR = PROJECT_DIR / "Интеграция с БД и агрегация данных (SQL + Backend)"
sys.path.insert(0, str(TASK_2_DIR))

from database import open_connection


def execute_sql_file(connection: object, file_path: Path) -> None:
    sql_script = file_path.read_text(encoding="utf-8")
    with connection.cursor() as cursor:
        cursor.execute(sql_script)


def main() -> None:
    schema_path = TASK_2_DIR / "sql" / "001_schema.sql"
    demo_data_path = TASK_2_DIR / "sql" / "002_demo_data.sql"
    with open_connection() as connection:
        execute_sql_file(connection, schema_path)
        execute_sql_file(connection, demo_data_path)
        connection.commit()
    print("База данных подготовлена. Добавлены партнёры и история продаж.")


if __name__ == "__main__":
    main()
