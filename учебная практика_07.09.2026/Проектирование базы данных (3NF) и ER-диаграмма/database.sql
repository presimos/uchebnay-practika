CREATE TABLE partners (
    partner_id INTEGER GENERATED ALWAYS AS IDENTITY,
    company_name VARCHAR(150) NOT NULL,
    inn VARCHAR(12) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,

    CONSTRAINT pk_partners
        PRIMARY KEY (partner_id),

    CONSTRAINT uq_partners_inn
        UNIQUE (inn),

    CONSTRAINT uq_partners_email
        UNIQUE (email)
);

CREATE TABLE products (
    product_id INTEGER GENERATED ALWAYS AS IDENTITY,
    product_name VARCHAR(150) NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL,

    CONSTRAINT pk_products
        PRIMARY KEY (product_id),

    CONSTRAINT chk_products_price
        CHECK (unit_price >= 0)
);

CREATE TABLE deliveries (
    delivery_id INTEGER GENERATED ALWAYS AS IDENTITY,
    partner_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    delivery_date DATE NOT NULL,
    quantity INTEGER NOT NULL,

    CONSTRAINT pk_deliveries
        PRIMARY KEY (delivery_id),

    CONSTRAINT fk_deliveries_partner
        FOREIGN KEY (partner_id)
        REFERENCES partners (partner_id),

    CONSTRAINT fk_deliveries_product
        FOREIGN KEY (product_id)
        REFERENCES products (product_id),

    CONSTRAINT chk_deliveries_quantity
        CHECK (quantity > 0)
);