class Main:
    def __init__(self):
        currentValue: float = 0

        while True:
            print(f"Current value {float(currentValue)}")

            number = input("Add number(empty stops): ")

            if number == "":
                print(f"Final value {float(currentValue)}")
                break
            else:
                try:
                    currentValue += float(number)
                except ValueError:
                    print("Invalid value.")

        return None
    
if __name__ == "__main__":
    app = Main()