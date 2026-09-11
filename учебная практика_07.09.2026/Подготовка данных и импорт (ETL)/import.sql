COPY partners (
    partner_id,
    company_name,
    inn,
    contact_email,
    phone,
    rating
)
FROM '/path/to/partners_clean.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8'
);

COPY sales (
    sale_id,
    partner_id,
    product_name,
    sale_date,
    quantity,
    total_amount
)
FROM '/path/to/sales_clean.txt'
WITH (
    FORMAT text,
    DELIMITER E'\\t',
    HEADER true,
    ENCODING 'UTF8'
);

SELECT COUNT(*) AS partners_count FROM partners;
SELECT COUNT(*) AS sales_count FROM sales;
