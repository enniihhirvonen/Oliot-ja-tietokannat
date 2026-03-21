import sys

class Main:
    def __init__(self) -> None:
        for line in sys.stdin:
            print(line.strip()[::-1])
        return None
    
if __name__ == "__main__":
    app = Main()