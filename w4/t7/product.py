from db_conn import DB_CONN
import sqlite3

class Product:
    cursor: sqlite3.Cursor
    manufacturer: str
    brand: str
    cost: float
    price: float
    def __init__(self, manufacturer: str, brand: str, cost: float, price: float) -> None:
        self.cursor = DB_CONN.cursor()
        self.manufacturer = manufacturer
        self.brand = brand
        self.cost = cost
        self.price = price
    @staticmethod
    def createProduct() -> 'Product':
        print("Insert product details below:")
        mfr = input("- Insert manufacturer: ")
        br = input("- Insert brand: ")
        cst = float(input("- Insert cost: "))
        pr = float(input("- Insert price: "))

        return Product(mfr, br, cst, pr)
    def insertDB(self) -> None:
        self.cursor.execute("INSERT INTO product(manufacturer, brand, cost, price) VALUES(?, ?, ?, ?)", (self.manufacturer, self.brand, self.cost, self.price)
        )
        return None
    @staticmethod
    def queryProducts(products: 'list[Product]' = []) -> 'list[Product]':
        cursor: sqlite3.Cursor = DB_CONN.cursor()
        cursor.execute("SELECT manufacturer, brand, cost, price FROM product")
        rows = cursor.fetchall()

        for mfr, br, cst, pr in rows:
            products.append(Product(mfr, br, cst, pr))
        return products
    