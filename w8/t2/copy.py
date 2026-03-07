import sys

class Main:
    def __init__(self) -> None:
        s_filepath = sys.argv[1]
        d_filepath = sys.argv[2]

        print(f"Copying {s_filepath} to {d_filepath}")

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