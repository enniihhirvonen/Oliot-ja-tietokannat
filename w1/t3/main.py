from counter import Counter

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        print("Initializing counter...")

        counter = Counter()

        print("Counter initialized.")

        while True:
            try:
                print("\nOptions:")
                print("1) Add count")
                print("2) Get count")
                print("3) Zero count")
                print("0) Exit program")

                choice = int(input("Choice: "))

                if choice == 1:
                    counter.addCount()
                    print("Count increased")
                elif choice == 2:
                    print(f"Current count '{counter.getCount()}'")
                elif choice == 3:
                    counter.zeroCount()
                    print("Count zeroed")
                elif choice == 0:
                    break
                else:
                    print("Invalid input.")
            except Exception as e:
                print(f"Error: {e}")

        print("\nProgram ending.")

        return None
    
if __name__ == "__main__":
    app = Main()