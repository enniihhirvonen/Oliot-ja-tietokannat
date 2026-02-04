class Main:
    def __init__(self) -> None:
        print("Program starting.")

        menu = Menu()

        menu.run()

        print("Program ending.")

        return None
    
class Menu:
    def run(self) -> None:
        while True:
            choice = -1
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottle")
            print("3 - Save bottle")
            print("0 - Exit")
            choice = self.ask_choice()
            if choice == 0:
                print("\nExiting program.")
                break
            elif choice == 1:
                print("'Add bottle' not implemented yet.")
            elif choice == 2:
                print("'Show bottle' not implemented yet.")
            elif choice == 3:
                print("'Save bottle' not implemented yet.")
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
    
if __name__ == "__main__":
    app = Main()