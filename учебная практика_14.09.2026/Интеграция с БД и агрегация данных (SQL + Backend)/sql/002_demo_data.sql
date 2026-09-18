INSERT INTO partners (
    partner_id,
    company_name,
    inn,
    contact_email,
    phone,
    rating
)
OVERRIDING SYSTEM VALUE
VALUES
    (1, 'ООО "Логистик-Экспресс"', '7701234567', 'info@logex.ru', '+79991112233', 4.8),
    (2, 'ИП Петров А.В.', '5001098765', 'petrov_delivery@mail.ru', NULL, 4.2),
    (3, 'ТК "Быстрый Путь"', '7812345678', 'speedway@yandex.ru', '+78125554433', NULL),
    (4, 'ООО "Новый партнёр"', '7700000004', 'new.partner@example.ru', '+79990000004', 5.0)
ON CONFLICT (partner_id) DO NOTHING;

INSERT INTO sales_history (
    sale_id,
    partner_id,
    product_name,
    sale_date,
    quantity,
    total_amount
)
VALUES
    (101, 1, 'Стиральный порошок "Альфа"', DATE '2026-03-01', 50, 25000.00),
    (102, 2, 'Мыло жидкое "Стандарт"', DATE '2026-03-15', 200, 18000.50),
    (103, 1, 'Кондиционер для белья', DATE '2026-03-20', 30, 10500.00),
    (105, 3, 'Мыло жидкое "Стандарт"', DATE '2026-03-25', 150, 13500.00)
ON CONFLICT (sale_id) DO NOTHING;

SELECT setval(
    pg_get_serial_sequence('partners', 'partner_id'),
    (SELECT MAX(partner_id) FROM partners)
);
