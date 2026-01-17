class Counter:
    def __init__(self) -> None:
        self.__count = 0
        return None
    def addCount(self) -> None:
        self.__count += 1
        return None
    def getCount(self) -> int:
        return self.__count
    def zeroCount(self) -> None:
        self.__count = 0
        return None