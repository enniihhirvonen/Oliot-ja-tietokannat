from db_conn import DB_CONN
import sqlite3

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

        menu = Menu(cursor)
        menu.run()

        DB_CONN.commit()
        
        print("Program ending.")

        cursor.close()
        DB_CONN.close()

        return None
    
class Menu:
    def __init__(self, cursor: sqlite3.Cursor) -> None:
        self.cursor = cursor
        return None
    def run(self) -> None:
        while True:
            print("Options:")
            print("1 - Add product")
            print("2 - Show products")
            print("0 - Exit")
            choice = self.askChoice()
            if choice == 0:
                break
            elif choice == 1:
                self.addProduct()
            elif choice == 2:
                self.showProducts()
        return None
    
    def askChoice(self) -> int:
        try:
            choice = int(input("Your choice: "))
            return choice
        except Exception as e:
            print(f"Error: {e}")
            pass
    
    def addProduct(self) -> None:
        print("Insert product details below:")
        manufacturer: str = input("- Insert manufacturer: ")
        brand: str = input("- Insert brand: ")
        cost: float = float(input("- Insert cost: "))
        price: float = float(input("- Insert price: "))

        print("Adding product...")

        self.cursor.execute("INSERT INTO product(manufacturer, brand, cost, price) VALUES(?, ?, ?, ?)", (manufacturer, brand, cost, price)
        )

        print("Product added!\n")
        return None
    
    def showProducts(self) -> None:
        self.cursor.execute("SELECT manufacturer, brand, cost, price FROM product")
        rows = self.cursor.fetchall()
        print("No., Manufacturer, Brand, Cost, Price")
        for i, row in enumerate(rows, start=1):
            print(f"{i}, {row[0]}, {row[1]}, {row[2]}, {row[3]}")
        print()
        return None
    
if __name__ == "__main__":
    app = Main()