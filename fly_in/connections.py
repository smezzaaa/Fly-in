from .errors import ParseError

class Connection:
    def __init__(self, name1, name2, data=None):
        self.name1 = name1
        self.name2 = name2
        self.capacity = 1
        self.data = data or []

    def check_data(self, msg):
        if not self.data:
            return
        if len(self.data) > 1:
            raise ParseError(f"{msg} extra keys in metadata:"
                            " expected one <max_link_capacity>")
        x = self.data[0]
        if x[0] != "max_link_capacity":
            raise ParseError(f"{msg} unknown key in metadata: expected <max_link_capacity>")
        try:
            cap = int(x[1])
        except ValueError as e:
            raise ValueError(f"{msg} : {e}")
        if cap <= 0:
            raise ParseError(f"{msg} invalid metadata value:"
                            " expected positive int for <max_link_capacity>")
    
    def extract_data(self):
        if not self.data:
            return
        x = self.data[0]
        self.capacity = int(x[1])