class Main:
    def __init__(self):
        try:
            number = int(input("Insert number: "))
            print(f"Inserted value is '{float(number)}'")
        except ValueError:
            print("Oops! That wasn't valid number.")

        return None
    
if __name__ == "__main__":
    app = Main()