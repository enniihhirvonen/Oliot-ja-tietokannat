class Person:
    first_name: str
    last_name: str
    __age: int
    def __init__(self, fname: str, lname: str, age: int) -> None:
        Person.first_name = fname
        Person.last_name = lname
        Person.__age = age
        return None
    def getAge(self) -> int:
        return Person.__age
    def ageUp(self) -> None:
        Person.__age += 1
        return None
    def getFullname(self) -> str:
        return f"{Person.first_name} {Person.last_name}"
    def printFullname(self) -> None:
        print(f"{Person.first_name} {Person.last_name}")
        return None