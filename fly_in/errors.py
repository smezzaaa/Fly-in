class ParseError(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f"{msg}!")

class MapError(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(f"{msg}!")