from db_conn import DB_CONN
from menu_product import MenuProduct

PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
manufacturer VARCHAR(255) NOT NULL,
brand VARCHAR(255) NOT NULL,
cost REAL NOT NULL,
price REAL NOT NULL
);
"""

class Main:
    def __init__(self) -> None:
        cursor = DB_CONN.cursor()

        print("Program starting.")

        cursor.execute(PRODUCT_TABLE_STATEMENT)

        menu = MenuProduct()
        menu.run()

        DB_CONN.commit()
        
        print("Program ending.")

        cursor.close()
        DB_CONN.close()

        return None
    
if __name__ == "__main__":
    app = Main()