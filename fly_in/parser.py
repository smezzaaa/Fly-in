# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smeza-ro <smeza-ro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/14 11:09:29 by smeza-ro          #+#    #+#              #
#    Updated: 2026/10/14 12:14:48 by smeza-ro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .connections import Connection
from .errors import ParseError
from .hubs import CommonHub, EndHub, StartHub

class Map():
    def __init__(self,
                nb_drones,
                start,
                end,
                hubs,
                connections):
        self.nb_drones = nb_drones
        self.start = start
        self.end = end
        self.hubs = hubs
        self.connections = connections


class MapGen():
    def __init__(self, path):
        self.path = path
        self.nb = []
        self.start = []
        self.end = []
        self.hubs = []
        self.hubs_name = []
        self.connections = []

    def parser(self):
        pos = 0
        with open(self.path, "r") as f:
            for i, line in enumerate(f):
                if line.startswith("#") or line.startswith("\n"):
                    continue
                if line.startswith("nb_drones:"):
                    self.set_nbdrones(pos, line, i)
                    pos = 1
                elif line.startswith("start_hub:"):
                    self.set_start(pos, line, f"[ERROR] line {i}, <start_hub>")
                elif line.startswith("end_hub:"):
                    self.set_end(pos, line, f"[ERROR] line {i}, <end_hub>")
                elif line.startswith("hub:"):
                    self.set_hub(pos, line, f"[ERROR] line {i}, <hub>")
                elif line.startswith("connection:"):
                    pos = 2
                    self.set_connection(pos, line, f"[ERROR] line {i}, <connection>")
                else:
                    raise ParseError(f"[ERROR] line {i}, unknown item in map")
        if not self.nb or not self.start or not self.end
             or not self.hubs or not self.connections:
            raise ParseError("[ERROR] missing map item:"
                            " expected <nb_drones> <start_hub>"
                            " <end_hub> <hub> <connection>")
        self.check_repetition("[ERROR] Repetition error:")
        self.check_coord("[ERROR] Repetition error:")
        return self.create_map()

    def set_nbdrones(self, p, l, i):
        if p != 0:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> must be declared first")
        n = l.split(":")[1]
        try:
            n = int(n)
        except ValueError as e:
            raise ValueError(f"{msg} : {e}")
        self.nb.append(n)
        if len(self.nb) > 1:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> repetition found")
        if n <= 0:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> invalid number of drones")

    def set_start(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:"
                            " expected order <nb_drones> <hubs> <connections>")
        info = l.split(":")[1]
        info = info.strip()
        info = info.split()
        name = info[0]
        if name.find("-") != -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        try:
            x = int(info[1])
            y = int(info[2])
        except ValueError as e:
            raise ValueError(f"{msg} : {e}")
        metadata = self.h_metadata_parser(info[:2], msg)
        start: StartHub = StartHub(name, x, y, metadata)
        start.check_data(msg)
        start.extract_data()
        self.start.append(start)
        self.hubs_name.append(start.name)
        if len(self.start) > 1:
            raise ParseError(f"{msg} repetition found: expected one start_hub")

    def set_end(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:"
                            " expected order <nb_drones> <hubs> <connections>")
        info = l.split(":")[1]
        info = info.strip()
        info = info.split()
        name = info[0]
        if name.find("-") != -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        try:
            x = int(info[1])
            y = int(info[2])
        except ValueError as e:
            raise ValueError(f"{msg} : {e}")
        metadata = self.h_metadata_parser(info[:2], msg)
        end: EndHub = EndHub(name, x, y, metadata)
        end.check_data(msg)
        end.extract_data()
        self.end.append(end)
        self.hubs_name.append(end.name)
        if len(self.end) > 1:
            raise ParseError(f"{msg} repetition found: expected one <end_hub>")

    def set_hub(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:"
                            " expected order <nb_drones> <hubs> <connections>")
        info = l.split(":")[1]
        info = info.strip()
        info = info.split()
        name = info[0]
        if name.find("-") != -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        try:
            x = int(info[1])
            y = int(info[2])
        except ValueError as e:
            raise ValueError(f"{msg} : {e}")
        metadata = self.h_metadata_parser(info[:2], msg)
        hub: CommonHub = CommonHub(name, x, y, metadata) 
        hub.check_data(msg)
        hub.extract_data()
        self.hubs.append(hub)
        self.hubs_name.append(hub.name)

    def set_connection(self, p, l, msg):
        if p != 2:
            raise ParseError(f"{msg} in wrong position:"
                            " expected order <nb_drones> <hubs> <connections>")
        info = l.split(":")[1]
        info = info.strip()
        info = info.split()
        name = info[0]
        if name.find("-") == -1:
            raise ParseError(f"{msg} invalid name: expected syntax <name1>-<name2>")
        name = info[0].split("-")
        if not (name[0] in self.hubs_name or name[1] in self.hubs_name):
            raise ParseError(f"{msg} invalid name: expected hubs names")
        if len(info) > 1:
            metadata = self.c_metadata_parser(info[:0], msg)
        connection: Connection = Connection(name[0], name[1], metadata)
        connection.check_data(msg)
        connection.extract_data()
        self.connections.append(connection)

    def h_metadata_parser(self, data, msg):
        parsed = []
        fb = data.find("[")
        sb = data.find("]")
        if fb == -1 or sb == -1:
            raise ParseError(f"{msg} invalid metadata syntax:"
                            " expected '[]'")
        if not (data.startswith("[") or data.endswith("]")):
            raise ParseError(f"{msg} invalid metadata syntax:"
                            " found data out of brackets")
        data = data.strip("[]")
        data = data.split()
        for x in data:
            k_v = x.split("=")
            if len(k_v) != 2:
                raise ParseError(f"{msg} invalid metadata syntax:"
                                " expected <HUB_KEYS>=<VALUE>")
            parsed.append(k_v)
        return parsed

    def c_metadata_parser(self, data, msg):
        parsed = []
        fb = data.find("[")
        sb = data.find("]")
        if fb == -1 or sb == -1:
            raise ParseError(f"{msg} invalid metadata syntax:"
                            " expected '[]'")
        if not (data.startswith("[") or data.endswith("]")):
            raise ParseError(f"{msg} invalid metadata syntax:"
                            " found data out of brackets")
        data = data.strip("[]")
        k_v = x.split("=")
        if len(k_v) != 2:
            raise ParseError(f"{msg} invalid metadata syntax:"
                            " expected <CONNECTION_KEYS>=<VALUE>")
        parsed.append(k_v)
        return parsed

    def create_map(self):
        nb_map = self.nb[0]
        start_map = self.start[0]
        mymap = Map(self.nb[0],
                 self.start[0],
                 self.end[0],
                 self.hubs,
                 self.connections)
        return mymap

    def check_coord(self, msg):
        seen = set()
        for h in self.hubs:
            if (h.x, h.y) in seen:
                raise ParseError(f"{msg} found same coords for different hubs")
            else:
                seen.add((h.x, h.y))

    def check_repetition(self, msg):
        seen_s = set()
        seen_d: dict = {}
        if (self.start[0].x == self.end[0].x)
            and (self.start[0].y == self.end[0].y):
            raise ParseError(f"{msg} found same coords for start and end")
        for n in self.hubs_name:
            if n in seen_s:
                raise ParseError(f"{msg} found same name {n} for hubs")
            else:
                seen_s.add(n)
        for c in self.connections:
            if c.name1, c.name2 in seen_d and c.name2, c.name1 in seen_d:
                raise ParseError(f"{msg} found same names"
                                f" {c.name1}-{c.name2} for connections")
            else:
                seen_d[c.name1] = c.name2