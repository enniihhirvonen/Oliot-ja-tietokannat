from product import Product

class MenuProduct:
    def __init__(self) -> None:
        pass
    def askChoice(self) -> int:
        choice: int = -1
        feed = input("Your choice: ")
        if feed.isdigit():
            choice = int(feed)
        return choice
    def showOptions(self) -> None:
        print("Options:")
        print("1 - Add product")
        print("2 - Show products")
        print("0 - Exit")
        return None
    def run(self) -> None:
        choice = -1
        while choice != 0:
            self.showOptions()
            choice = self.askChoice()
            if choice == 0:
                pass
            elif choice == 1:
                self.addProduct()
            elif choice == 2:
                self.showProducts()
            else:
                print("Unknown option.")
        return None
    def addProduct(self) -> None:
        product = Product.createProduct()
        print("Adding product...")
        product.insertDB()
        print("Product added!\n")
        return None
    def showProducts(self) -> None:
        products = Product.queryProducts()
        print("No., Manufacturer, Brand, Cost, Price")
        for i, product in enumerate(products, start = 1):
            print(f"{i}, {product.manufacturer}, {product.brand}, {product.cost}, {product.price}")
        print()
        return None