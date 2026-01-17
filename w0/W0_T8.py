from math import pi, tau

class Main:
    def __init__(self):
        if tau == pi:
            print("Tau equals Pi.")
        else:
            print("Tau doesn't equal Pi.")
        
        if tau == (2 * pi):
            print("Tau equals 2 * Pi.")
        else:
            print("Tau doesn't equal 2 * Pi.")

        return None
    
if __name__ == "__main__":
    app = Main()