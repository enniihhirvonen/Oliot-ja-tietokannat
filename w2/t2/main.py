from soda_bottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        filename: str = input("Insert filename: ")

        with open(filename, "r") as file:
            line: str = file.readline().strip()

        print(f"Deserializing \"{line}\"")

        SodaBottle.deserialize(line)

        print("Program ending.")

        return None
    
if __name__ == "__main__":
    app = Main()