class Main:
    def __init__(self):
        print("Per Miller's Law, humans can retain ~7 items in short-term memory.")
        memString = input("Insert memorable string: ")

        if len(memString) <= 7:
            print("This string will be easy to remember.")
        else:
            print("This string will be hard to remember.")

        return None
    
if __name__ == "__main__":
    app = Main()