class ParseError(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        self.line = line
        super().__init__(f"{msg}!\n")
