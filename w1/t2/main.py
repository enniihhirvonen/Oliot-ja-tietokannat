from car import Car

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        print("Initializing three car objects.")

        c1 = Car("red")
        c2 = Car("green")
        c3 = Car("blue")

        print("Car objects initialized.")

        print("Starting the first car object.")
        c1.start()

        print("Starting the second car object.")
        c2.start()

        print("Starting the third car object.")
        c3.start()

        print("Starting the third car object.")
        c3.start()

        print("Program ending.")

        return None
    
if __name__ == "__main__":
    app = Main()