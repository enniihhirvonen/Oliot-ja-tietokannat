import sys

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Main:
    def __init__(self) -> None:
        message = sys.argv[1]
        decrypted_message = ""

        for char in message:
            if char in LOWER_ALPHABETS:
                char_idx = LOWER_ALPHABETS.index(char)
                decrypted_idx = (char_idx - 13) % 26
                decrypted_message += LOWER_ALPHABETS[decrypted_idx]
            elif char in UPPER_ALPHABETS:
                char_idx = UPPER_ALPHABETS.index(char)
                decrypted_idx = (char_idx - 13) % 26
                decrypted_message += UPPER_ALPHABETS[decrypted_idx]
            else:
                decrypted_message += char
                pass

        print(decrypted_message)

        return None

if __name__ == "__main__":
    app = Main()