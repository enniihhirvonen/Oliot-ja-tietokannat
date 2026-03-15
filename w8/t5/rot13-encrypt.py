import sys

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Main:
    def __init__(self) -> None:
        message = " ".join(sys.argv[1:])
        encrypted_message = ""

        for char in message:
            if char in LOWER_ALPHABETS:
                char_idx = LOWER_ALPHABETS.index(char)
                encrypted_idx = (char_idx + 13) % 26
                encrypted_message += LOWER_ALPHABETS[encrypted_idx]
            elif char in UPPER_ALPHABETS:
                char_idx = UPPER_ALPHABETS.index(char)
                encrypted_idx = (char_idx + 13) % 26
                encrypted_message += UPPER_ALPHABETS[encrypted_idx]
            else:
                encrypted_message += char
                pass

        print(encrypted_message)

        return None

if __name__ == "__main__":
    app = Main()