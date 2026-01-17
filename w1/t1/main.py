from person import Person

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        print("Initializing persons...")

        p1 = Person("Jane", "Morgan")
        p2 = Person("John", "Doe")

        print("Persons initialized, names below.")

        p1.fullname()
        p2.fullname()

        print("Program ending.")
        return None
    
if __name__ == "__main__":
    app = Main()