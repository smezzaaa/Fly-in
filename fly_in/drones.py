from .a_star import a_star

class Drone():
    def __init__(self, goal, id, coord, pos):
        self.goal = goal
        self.id = id
        self.coord = coord
        self.path = []
        self.pos = pos
    
    def get_new_path(self):
        self.path.append(a_star(self.pos, self.goal))
        return self.path

    def has_landed(self):
        if self.pos == self.goal:
            return True
        return False