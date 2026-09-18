import os


def open_connection() -> object:
    database_url = os.environ.get("DATABASE_URL")

    try:
        import psycopg
    except ImportError as error:
        message = "Установите зависимости: python -m pip install -r requirements.txt"
        raise RuntimeError(message) from error

    if database_url:
        return psycopg.connect(database_url)

    return psycopg.connect()