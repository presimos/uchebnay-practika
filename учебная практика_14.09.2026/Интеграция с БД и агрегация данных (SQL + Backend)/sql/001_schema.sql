CREATE TABLE IF NOT EXISTS partners (
    partner_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    inn VARCHAR(12) NOT NULL UNIQUE,
    contact_email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    rating NUMERIC(2, 1),
    CONSTRAINT chk_partners_rating
        CHECK (rating IS NULL OR rating BETWEEN 0 AND 5)
);

CREATE TABLE IF NOT EXISTS sales_history (
    sale_id INTEGER PRIMARY KEY,
    partner_id INTEGER NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    sale_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL,
    CONSTRAINT fk_sales_history_partner
        FOREIGN KEY (partner_id)
        REFERENCES partners (partner_id)
        ON DELETE RESTRICT,
    CONSTRAINT chk_sales_history_quantity
        CHECK (quantity > 0),
    CONSTRAINT chk_sales_history_total_amount
        CHECK (total_amount >= 0)
);

CREATE INDEX IF NOT EXISTS idx_sales_history_partner_id
    ON sales_history (partner_id);
