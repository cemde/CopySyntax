

pandas_prefix = "pd."
numpy_prefix = "np."
pytorch_prefix= "torch."

# https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed
# for checking if package is installed


class Literal:
    def __init__(self, string, type) -> None:
        self.string = string
        self.type = type
    
    def __str__(self):
        return self.string
    
    def print(self):
        self.__str__()
    
    def clipboard(self):
        pass
    
    def save(self, file):
        pass

def syntax(obj, quotes="single", line_length=-1):
    if isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = '"' + obj + '"'
    elif isinstance(obj, list):
        val = [syntax(element) for element in obj]
        val = "[" + ",".join(val) + "]"
    elif isinstance(obj, dict):
        val = [f"{syntax(key)}: {syntax(val)}" for key, val in obj.items()]
        val = "{" + ",".join(val) + "}"
    elif isinstance(obj, tuple):
        val = [syntax(element) for element in obj]
        val = "(" + ",".join(val) + ",)"
    return val


print(syntax({'5': 1, 'blo': 4}))
print(syntax((1, 5, 4,)))


