from .errors import ParseError

HUBS_KEYS = {"zone", "color", "max_drones"}
COLOR_KEYS = {"red", "green", "yellow", "blue", "grey"}
ZONE_KEYS = {"normal", "restricted", "priority", "blocked"}


class Hubs():
    def __init__(self, name, x, y, data: list | None):
        self.name = name
        self.x = x
        self.y = y
        self.color = "grey"
        self.zone = "normal"
        self.max = 1
        self.data = data


class StartHub(Hubs):
    def __init__(self, name, x, y, data):
        super().__init__(name, x, y, data)
        self.msg = f"[ERROR] <start_hub> {name}"
        self.max = float("inf")

    def check_data(self):
        seen = set()
        if len(self.data) > 3:
            raise ParseError(f"{self.msg} extra keys in metadata: expected three from <HUB_KEYS>")
        for x in self.data:
            k = x[0]
            v = x[1]
            if k in seen:
                raise ParseError(f"{self.msg} duplicated key in metadata")
            if k not in HUB_KEYS:
                raise ParseError(f"{self.msg} unknown key in metadata: expected <HUB_KEYS>")
            if k == "color":
                if v not in COLOR_KEYS:
                    raise ParseError(f"{self.msg} invalid metadata value: expected <COLOR_KEYS>")
            seen.add(k)

    def extract_data(self):
        for x in self.data:
            k = x[0]
            v = x[1]
            if k == "color":
                self.color = v



class EndHub(Hubs):
    def __init__(self, name, x, y, data):
        super().__init__(name, x, y, data)
        self.msg = f"[ERROR] <end_hub> {name}"
        self.max = float("inf")

    def check_data(self):
        seen = set()
        if len(self.data) > 3:
            raise ParseError(f"{self.msg} extra keys in metadata: expected three from <HUB_KEYS>")
        for x in self.data:
            k = x[0]
            v = x[1]
            if k in seen:
                raise ParseError(f"{self.msg} duplicated key in metadata")
            if k not in HUB_KEYS:
                raise ParseError(f"{self.msg} unknown key in metadata: expected <HUB_KEYS>")
            if k == "color":
                if v not in COLOR_KEYS:
                    raise ParseError(f"{self.msg} invalid metadata value: expected <COLOR_KEYS>")
            seen.add(k)
    
    def extract_data(self):
        for x in self.data:
            k = x[0]
            v = x[1]
            if k == "color":
                self.color = v


class CommonHub(Hubs):
    def __init__(self, name, x, y, data):
        super().__init__(name, x, y, data)
        self.msg = f"[ERROR] <hub> {name}"

    def check_data(self):
        seen = set()
        if len(self.data) > 3:
            raise ParseError(f"{self.msg} extra keys in metadata: expected three from <HUB_KEYS>")
        for x in self.data:
            k = x[0]
            v = x[1]
            if k in seen:
                raise ParseError(f"{self.msg} duplicated key in metadata")
            if k not in HUB_KEYS:
                raise ParseError(f"{self.msg} unknown key in metadata: expected <HUB_KEYS>")
            if k == "color":
                if v not in COLOR_KEYS:
                    raise ParseError(f"{self.msg} invalid metadata value: expected <COLOR_KEYS>")
            elif k == "zone":
                if v not in ZONE_KEYS:
                    raise ParseError(f"{self.msg} invalid metadata value: expected <ZONE_KEYS>")
            elif k == "max_drones":
                v = int(v)
                if v <= 0:
                    raise ParseError(f"{self.msg} invalid metadata value:"
                                    " expected positive int for <max_drones>")
            seen.add(k)

    def extract_data(self):
        for x in self.data:
            k = x[0]
            v = x[1]
            if k == "color":
                self.color = v
            elif k == "zone":
                self.zone = v
            elif k == "max_drones":
                self.max = int(v)