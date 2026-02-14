from person import Person

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Creating person...")

        p1 = Person("John", "Doe", 30)

        print("Person created.")

        print(f"Name: {p1.getFullname()}")
        print(f"Age: {p1.getAge()}")

        print("Person has now birthday...")
        p1.ageUp()
        age = p1.getAge()
        print(f"New age: {age}")

        print("Program ending.")

        return None
    
if __name__ == "__main__":
    app = Main()