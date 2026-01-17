class Main:
    def __init__(self):
        filename = input("Insert filename to read: ")

        try:
            with open(filename, "r") as file:
                rows = file.readlines()
                content = "".join(rows)

            print(f"#### {filename} content ####")
            print(content)
            print(f"#### {filename} content ####")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

        return None
    
if __name__ == "__main__":
    app = Main()