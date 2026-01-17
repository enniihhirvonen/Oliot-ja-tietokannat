class Car:
    engine_on: bool
    color: str
    def __init__(self, color: str) -> None:
        self.engine_on = False
        self.color = color
        return None
    def start(self) -> None:
        if self.engine_on:
            print(f"{self.color} is already running.")
        else:
            print(self.color + " car started.")
            self.engine_on = True
        return None