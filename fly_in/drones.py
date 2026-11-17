from .a_star import a_star

class Drone():
    def __init__(self, start, goal, id, coord, status):
        self.start = start
        self.goal = goal
        self.id = id
        self.coord = coord
        self.path = []
        self.status = []

    def space_time_path(self, nb_drones):
        st_path = []
        for curr in self.path:
            count = 0
            if curr == self.start:
                count += self.id + 1
            if curr == self.goal:
                count = nb_drones - self.id
            else:
                count += 1
            #elif curr.t_cost == 2.0:
            #    count += 2             non mi serve visto che la tabella st la scrivo su drone_scheduler

            for i in range(0, count):
                st_path.append(curr)
        return st_path

    def create_new_path(self):
        self.path = (a_star(self.start, self.goal, self.id))

    def has_landed(self):
        if self.pos == self.goal:
            return True
        return False