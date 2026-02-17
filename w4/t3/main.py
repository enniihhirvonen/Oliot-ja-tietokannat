from db_conn import DB_CONN

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Program ending.")
        DB_CONN.close()
        return None
    
if __name__ == "__main__":
    app = Main()