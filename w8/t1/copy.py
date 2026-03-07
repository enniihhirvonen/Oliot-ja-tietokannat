class Main:
    def __init__(self) -> None:
        print("Welcome to the copy utility.")

        s_filepath = input("Insert source filepath: ")
        d_filepath = input("Insert destination filepath: ")

        content: list[bytes] = []

        with open(s_filepath, "rb") as s:
            line = s.readlines()
            content.extend(line)

        with open(d_filepath, "wb") as d:
            d.writelines(content)

        print("Copy operation completed!")
        
        return None

if __name__ == "__main__":
    app = Main()