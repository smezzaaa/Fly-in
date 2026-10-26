"""Hub models and metadata validation."""

from .errors import ParseError

HUB_KEYS = {"zone", "color", "max_drones"}
ZONE_KEYS = {"normal", "blocked", "restricted", "priority"}
COLOR_KEYS = {"green", "blue", "white", "red"}


class Hubs:
    def __init__(self, name, x, y, data=None):
        self.name = name
        self.x = x
        self.y = y
        self.color = "none"
        self.zone = "normal"
        self.max = 1
        self.data = data or []

    def _validate_metadata(self, msg, unlimited_capacity=False):
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

    def _extract_metadata(self, unlimited_capacity=False):
        for key, value in self.data:
            if key == "zone":
                self.zone = value
            elif key == "color":
                self.color = value
            elif key == "max_drones" and not unlimited_capacity:
                self.max = int(value)


class StartHub(Hubs):
    def __init__(self, name, x, y, data=None):
        super().__init__(name, x, y, data)
        self.max = float("inf")

    def check_data(self, msg):
        self._validate_metadata(msg, unlimited_capacity=True)

    def extract_data(self):
        self._extract_metadata(unlimited_capacity=True)


class EndHub(Hubs):
    def __init__(self, name, x, y, data=None):
        super().__init__(name, x, y, data)
        self.max = float("inf")

    def check_data(self, msg):
        self._validate_metadata(msg, unlimited_capacity=True)

    def extract_data(self):
        self._extract_metadata(unlimited_capacity=True)


class CommonHub(Hubs):
    def check_data(self, msg):
        self._validate_metadata(msg)

    def extract_data(self):
        self._extract_metadata()