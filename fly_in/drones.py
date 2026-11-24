from .a_star import a_star
from .errors import MapError

class Drone():
    def __init__(self, start, goal, id, coord, status):
        self.start = start
        self.goal = goal
        self.id = id
        self.coord = coord
        self.path = {}
        self.status = {}

    def booking_hub(self):
        for i, (curr, t) in enumerate(self.path):
            if curr is self.start or curr is self.goal:
                continue

            if curr.zone == "restricted" and i > 0:
                previous_hub = self.path[i - 1][0]

                # Waiting in the same hub doesn't use a connection.
                if previous_hub is not curr:
                    connection = curr.get_connection(previous_hub)
                    if connection is None:
                        raise MapError(
                            f"[ERROR]: connection "
                            f"{previous_hub.name}-{curr.name} has not been found"
                        )
                    connection.book(t - 1)

            curr.book(t)

    def create_new_path(self):
        self.path = (a_star(self.start, self.goal, self))
        if not self.path:
            raise MapError("[ERROR]: no path has been found")
        print(f"=== DRONE {self.id} ===")
        for ht in self.path:
            print(f"in {ht[0].name} at turn {ht[1]}") # memo: in a_star {hub:turn} in status {turn:hub}

    def set_status(self):
        for ht in self.path:
            self.status[ht[1]] = ht[0]

    def move_to(self, hub, t):
        self.status[t] = hub

    def has_landed(self):
        if self.pos == self.goal:
            return True
        return False