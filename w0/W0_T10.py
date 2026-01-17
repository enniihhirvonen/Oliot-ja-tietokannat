class Main:
    def __init__(self):
        word: str = input("Insert word: ")
        searchTerm: str = input("Insert search term: ")

        if searchTerm in word:
            print(f"Search term '{searchTerm}' do appear in word '{word}'")
        else:
            print(f"Search term '{searchTerm}' doesn't appears in word '{word}'")

        return None
    
if __name__ == "__main__":
    app = Main()