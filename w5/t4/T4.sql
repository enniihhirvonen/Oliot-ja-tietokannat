CREATE TABLE product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE NOT NULL,
price_per_kilo NUMERIC NOT NULL
);
CREATE TABLE receipt (
id INTEGER PRIMARY KEY AUTOINCREMENT,
cashier TEXT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE product_receipt (
amount NUMERIC NOT NULL,
product_id INTEGER NOT NULL,
receipt_id INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES product(id),
FOREIGN KEY (receipt_id) REFERENCES receipt(id)
);
.mode csv
.import --skip 1 t4_product.csv product
.import --skip 1 t4_receipt.csv receipt
.import --skip 1 t4_product_receipt.csv product_receipt
