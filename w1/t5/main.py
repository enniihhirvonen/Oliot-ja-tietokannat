from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")

        coin_a = CoinAcceptor()

        while True:
            try:
                choice = input("\nInsert coin(0 return, -1 exit): ")

                if choice == "-1":
                    print("Exiting program.")
                    break
                elif choice == "0":
                    print("Returning coins...")
                    print(f"{coin_a.getAmount()} coins with {coin_a.getValue()}€ value returned.")
                    coin_a.returnCoins()
                    
                elif float(choice) > 0:
                    print("Inserting...")
                    coin_a.insertCoin(float(choice))

                if coin_a.getValue() == 0.0:
                    print(f"Inserted coins - {coin_a.getAmount()}, value - {coin_a.getValue():g}€") # :g makes it so if the value is 0, it won't print the decimal because test is being annoying pt. 2 :)
                    # ive tried fixing this like 3 times now hopefully the test accepts it this time.........
                else:
                    print(f"Inserted coins - {coin_a.getAmount()}, value - {coin_a.getValue()}€")
            except Exception as e:
                print(f"Error: {e}")

        print("\nProgram ending.")

        return None
    
if __name__ == "__main__":
    app = Main()