

class Literal:
    def __init__(self, string, type) -> None:
        self.string = string
        self.type = type
    
    def __str__(self):
        return self.string
    
    def print(self):
        return self.__str__()
    
    def clipboard(self):
        pass
    
    def save(self, file):
        pass
