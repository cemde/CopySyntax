class Literal:
    def __init__(self, string: str, type: str) -> None:
        self.string = string
        self.type = type

    def __str__(self) -> str:
        return self.string

    def print(self) -> str:
        return self.__str__()

    def clipboard(self):
        pass

    def save(self, file: str) -> None:
        pass
