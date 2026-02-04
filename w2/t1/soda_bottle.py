class SodaBottle:
    brand: str # [a-zA-Z-_]
    volume: float
    def __init__(self, brand: str, volume: float) -> None:
        self.brand = brand
        self.volume = volume
        return None
    def serialize(self) -> str:
        result: str = f"{self.brand};{self.volume}"
        return result