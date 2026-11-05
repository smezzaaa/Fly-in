from .connections import Connection
from .errors import ParseError
from .hubs import Hub, EndHub, StartHub
from .a_star import a_star
from .drones import Drone

class Map:
    def __init__(self,
                 nb_drones,
                 start,
                 end,
                 hubs,
                 connections):
        self.nb_drones = nb_drones
        self.drones = []
        self.start: StartHub = start
        self.end: EndHub = end
        self.hubs: list[Hub] = hubs
        self.connections: list[Connection] = connections

    def create_drones(self):
        for i in range (1, self.nb_drones):
            self.drones.append(Drone(self.end, i, self.start.coord, self.start))
        for d in self.drones:
            print(f"Drone n.{d.id}, coord{d.coord}")

    def get_path(self):
        path = a_star(self.start, self.end)
        for x in path:
            print(f"{x.name}")