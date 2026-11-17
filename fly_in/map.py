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
        for i in range (0, self.nb_drones):
            self.drones.append(Drone(self.start, self.end, i, self.start.coord, (0, self.start)))

    def initialize_hub_cost(self):
        for h in self.hubs:
            if h.zone == "priority":
                h.t_cost = 0.9
            if h.zone == "restricted":
                h.t_cost = 2.0
