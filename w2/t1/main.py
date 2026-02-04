from soda_bottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Constructing soda bottle.")

        brand = str(input("Insert brand: "))
        volume = float(input("Insert volume: "))

        bottle = SodaBottle(brand, volume)

        print("SodaBottle object created!")
        print("Serializing SodaBottle object.")

        result = SodaBottle.serialize(bottle)

        print("Serialized sodabottle:")

        print(result)

        print("Program ending.")

        return None
    
if __name__ == "__main__":
    app = Main()