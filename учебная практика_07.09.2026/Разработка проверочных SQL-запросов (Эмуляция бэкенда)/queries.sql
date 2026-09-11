SELECT
    p.partner_id,
    p.company_name,
    COUNT(d.delivery_id) AS deliveries_count
FROM partners p
LEFT JOIN deliveries d
    ON p.partner_id = d.partner_id
GROUP BY
    p.partner_id,
    p.company_name
ORDER BY
    p.company_name;

BEGIN;

-- Создание нового партнёра
INSERT INTO partners (
    company_name,
    inn,
    email,
    phone,
    address
)
VALUES (
    'ООО Тестовый партнёр',
    '7800000001',
    'test@partner.ru',
    '+7 900 000-00-01',
    'г. Санкт-Петербург'
)
RETURNING partner_id;

INSERT INTO deliveries (
    partner_id,
    product_id,
    delivery_date,
    quantity
)
VALUES (
    (SELECT partner_id
     FROM partners
     WHERE inn = '7800000001'),
    1,
    CURRENT_DATE,
    10
);

COMMIT;

SELECT
    p.company_name,
    pr.product_name,
    d.delivery_date,
    d.quantity,
    (d.quantity * pr.unit_price) AS total_amount
FROM deliveries d
JOIN partners p
    ON d.partner_id = p.partner_id
JOIN products pr
    ON d.product_id = pr.product_id
WHERE p.partner_id = 1
  AND d.delivery_date BETWEEN '2026-01-01' AND '2026-12-31'
ORDER BY d.delivery_date;
