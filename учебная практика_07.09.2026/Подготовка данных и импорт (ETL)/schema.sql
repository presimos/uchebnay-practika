DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS partners;

CREATE TABLE partners (
    partner_id INT PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    inn VARCHAR(12) NOT NULL UNIQUE,
    contact_email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    rating DECIMAL(2,1),

    CONSTRAINT chk_partners_rating
        CHECK (rating IS NULL OR (rating >= 0 AND rating <= 5))
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    partner_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,

    CONSTRAINT fk_sales_partner
        FOREIGN KEY (partner_id)
        REFERENCES partners(partner_id)
        ON DELETE RESTRICT,

    CONSTRAINT chk_sales_quantity
        CHECK (quantity > 0),

    CONSTRAINT chk_sales_total_amount
        CHECK (total_amount >= 0)
);
