"""Hub models and metadata validation."""

from .errors import ParseError, MapError

HUB_KEYS = {"zone", "color", "max_drones"}
ZONE_KEYS = {"normal", "blocked", "restricted", "priority"}
COLOR_KEYS = {"green", "blue", "white", "red", "yellow", "orange"}


class Hub:
    def __init__(self, name, coord, data=None):
        self.name = name
        self.coord = coord
        self.color = "none"
        self.zone = "normal"
        self.max_c = 1
        #self.capacity = 0
        #self.available = True
        self.status = {}
        self.data = data or []
        self.connection = set()
        self.n_hubs = set()
        self.t_cost = 1.0
        self.h_cost = float("inf")
        self.g_cost = 0.0
        self.blocked = False
        self.parent = None

    def validate_metadata(self, msg, unlimited_capacity=False):
        seen = set()
        for key, value in self.data:
            if key in seen:
                raise ParseError(f"{msg}: duplicated metadata key")
            if key not in HUB_KEYS:
                raise ParseError(f"{msg}: unknown metadata key")
            seen.add(key)
            if key == "zone" and value not in ZONE_KEYS:
                raise ParseError(f"{msg}: invalid zone type")
            elif key == "color" and value not in COLOR_KEYS:
                raise ParseError(f"{msg}: invalid color type")
            # Capacity metadata on start/end is explicitly ignored, including its value.
            if key == "max_drones" and not unlimited_capacity:
                try:
                    capacity = int(value)
                except ValueError as error:
                    raise ParseError(
                        f"{msg}: max_drones must be a positive integer"
                    ) from error
                if capacity <= 0:
                    raise ParseError(f"{msg}: max_drones must be a positive integer")

    def extract_metadata(self, unlimited_capacity=False):
        for key, value in self.data:
            if key == "zone":
                self.zone = value
                if self.zone == "blocked":
                    self.blocked = True
            elif key == "color":
                self.color = value
            elif key == "max_drones" and not unlimited_capacity:
                self.max_c = int(value)

    def get_cost(self):
        return self.g_cost + self.h_cost

    def connect_to(self, msg, n, connection):
        if self.name == n.name:
            raise ParseError(f"{msg} invalid connection: expected 2 different names")
        if self.blocked or n.blocked:
            return
        self.n_hubs.add(n)
        self.connection.add(connection)
        n.n_hubs.add(self)
        n.connection.add(connection)

    def get_neighbour(self):
        return self.n_hubs.copy()

    def is_available(self):
        if self.capacity == self.max_c:
            self.available = False
        return self.available

    def add_drone(self):
        self.capacity += 1
        if self.capacity > self.max_link_capacity:
            raise MapError(f"[ERROR] too many drones on hub <{self.name}>>")


class StartHub(Hub):
    def __init__(self, name, coord, data=None):
        super().__init__(name, coord, data)
        self.max_c = float("inf")

    def check_data(self, msg):
        self.validate_metadata(msg, unlimited_capacity=True)

    def extract_data(self):
        self.extract_metadata(unlimited_capacity=True)


class EndHub(Hub):
    def __init__(self, name, coord, data=None):
        super().__init__(name, coord, data)
        self.max_c = float("inf")

    def check_data(self, msg):
        self.validate_metadata(msg, unlimited_capacity=True)

    def extract_data(self):
        self.extract_metadata(unlimited_capacity=True)
