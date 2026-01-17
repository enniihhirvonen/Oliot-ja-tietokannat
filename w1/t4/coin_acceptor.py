class CoinAcceptor:
    def __init__(self) -> None:
        self.__amount: int = 0
        self.__value: float = 0.0
        return None
    def insertCoin(self) -> None:
        self.__amount += 1
        return None
    def getAmount(self) -> int:
        return self.__amount
    def returnCoins(self) -> int:
        return_amount = self.__amount
        self.__amount = 0
        return return_amount
