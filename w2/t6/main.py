from soda_bottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Loading inventory...")

        inventory = Inventory()
        loaded_bottles = inventory.load()

        print("Inventory loaded.")

        menu = Menu(loaded_bottles, inventory)
        menu.run()

        print("Program ending.")

        return None
    
class Inventory:
    def load(self) -> list[SodaBottle]:
        bottles: list[SodaBottle] = []
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    bottles.append(SodaBottle.deserialize(line))
        return bottles
    
    def save(self, bottles: list[SodaBottle]) -> None:
        with open("inventory.txt", "w") as file:
            for bottle in bottles:
                file.write(bottle.serialize() + "\n")
    
class Menu:
    def __init__(self, bottles: list[SodaBottle], inventory: Inventory) -> None:
        self.bottles = bottles
        self.inventory = inventory
        return None

    def run(self) -> None:
        while True:
            choice = -1
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottles")
            print("3 - Save bottle")
            print("0 - Exit")
            choice = self.ask_choice()
            if choice == 0:
                print("\nExiting program.")
                break
            elif choice == 1:
                print("Creating soda bottle.")
                self.add_bottle()
            elif choice == 2:
                self.show_bottles()
            elif choice == 3:
                print("Saving soda bottles...")
                self.save_bottles()
                print("Saving completed!")
            else:
                print("Unknown option, try again.")
            print("")
        return None

    def ask_choice(self) -> int:
        choice = -1
        feed = input("Your choice: ")
        if feed.isdigit():
            choice = int(feed)
        return choice
    
    def add_bottle(self) -> None:
        brand = input("Insert brand: ")
        volume = float(input("Insert volume: "))
        bottle = SodaBottle(brand, volume)
        self.bottles.append(bottle)
        return None
    
    def show_bottles(self) -> None:
        print("#### Soda bottles ####")
        
        for i, bottle in enumerate(self.bottles, start = 1):
            print(f"Bottle {i}:")
            print(f"  brand - {bottle.brand}")
            print(f"  volume - {bottle.volume}")

        print("#### Soda bottles ####")
        return None

    def save_bottles(self) -> None:
        self.inventory.save(self.bottles)
        return None
    
if __name__ == "__main__":
    app = Main()