HUBS_KEYS = {"zone", "color", "max_drones"}
COLOR_KEYS = {"red", "green", "yellow", "blue", "grey"}
ZONE_KEYS = {"normal", "restricted", "priority", "blocked"}


class Hubs():
    def __init__(self, name, x, y, data | None):
        self.name = name
        self.x = x
        self.y = y
        self.color = "grey"
        self.zone = "normal"
        self.max = 1
        if data:
            self.data = data

        def extract_data(self):
        for x in self.data:
            k = x[0]
            v = x[1]
            if k == "color":
                self.color = v
            elif k == "zone":
                self.zone = v
            elif k == "max_drones"
                self.max = int(v)


class StartHub(Hubs):
    def __init__(self, name, x, y, data | None):
        super().__init__(name, x, y)
        self.msg = f"[ERROR] <start_hub> {name}"
        self.max = float(inf)

    def check_data(self):
        seen = ()
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
            seen.append(k)



class EndHub(Hubs):
    def __init__(self, name, x, y):
        super().__init__(name, x, y, data)
        self.msg = f"[ERROR] <end_hub> {name}"
        self.max = float(inf)

    def check_data(self):
        seen = ()
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
            seen.append(k)


class CommonHub(Hubs):
    def __init__(self, name, x, y, data):
        super().__init__(name, x, y)
        self.msg = f"[ERROR] <hub> {name}"

    def check_data(self):
        seen = ()
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
            if k == "zone":
                if v not in ZONE_KEYS:
                    raise ParseError(f"{self.msg} invalid metadata value: expected <ZONE_KEYS>")
            if k == "max_drones":
                v = int(v)
                if v < 0:
                    raise ParseError(f"{self.msg} invalid metadata value:
                                     expected positive int for <max_drones>")
            seen.append(k)
