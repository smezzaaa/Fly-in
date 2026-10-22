class ParseError(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f"{msg}!\n")

class MyValueError(ValueError):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f"{msg}!\n")