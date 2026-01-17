from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        coin_a = CoinAcceptor()

        first = True

        while True:
            try:
                if not first: 
                    print() # print a blank line only AFTER the first iteration because the test is being annoying :)

                first = False
                
                print("1 - Insert coin")
                print("2 - Show coins")
                print("3 - Return coins")
                print("0 - Exit program")

                choice = int(input("Your choice: "))

                if choice == 1:
                    coin_a.insertCoin()
                elif choice == 2:
                    print(f"Currently '{coin_a.getAmount()}' coins in coin acceptor")
                elif choice == 3:
                    
                    print(f"Coin acceptor returned '{coin_a.returnCoins()}' coins.")
                elif choice == 0:
                    break
                else:
                    print("Invalid input.")
            except Exception as e:
                print(f"Error: {e}")

        print("Program ending.")

        return None
    
if __name__ == "__main__":
    app = Main()