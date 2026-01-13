class Main:
    def __init__(self):
        age = int(input("Insert age: "))

        if age >= 18:
            print("Adult")
        else:
            print("Child")

        return None
    
if __name__ == "__main__":
    app = Main()