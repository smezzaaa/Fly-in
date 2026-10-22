from .errors import ParseError

class Connection():
    def __init__(self, name1, name2, data: list | None):
        self.name1 = name1
        self.name2 = name2
        self.capacity = 1
        self.msg = f"[ERROR] <connections> {name1}-{name2}"
        if data:
            self.data = data

    def check_data(self):
        if len(self.data) > 1:
            raise ParseError(f"{self.msg} extra keys in metadata:"
                            " expected one <max_link_capacity>")
        x = self.data[0]
        if x[0] != "max_link_capacity":
            raise ParseError(f"{self.msg} unknown key in metadata: expected <max_link_capacity>")
        if int(x[1]) < 0:
            raise ParseError(f"{self.msg} invalid metadata value:"
                            " expected positive int for <max_link_capacity>")
    
    def extract_data(self):
        x = self.data[0]
        self.capacity = int(x[1])