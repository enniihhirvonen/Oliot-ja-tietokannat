class CoinAcceptor:
    def __init__(self) -> None:
        self.__amount: int = 0
        self.__value: float = 0.0
        return None
    def insertCoin(self, choice: float) -> None:
        self.__amount += 1
        self.__value += choice
        return None
    def getAmount(self) -> int:
        return self.__amount
    def getValue(self) -> float:
        return self.__value
    def returnCoins(self) -> tuple[int, float]:
        return_amount = self.__amount
        return_value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return return_amount, return_value
