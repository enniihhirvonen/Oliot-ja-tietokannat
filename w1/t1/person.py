class Person:
    first_name: str
    last_name: str
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname
        return None
    def fullname(self) -> None:
        print(self.fname + " " + self.lname)
        return None
