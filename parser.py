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

HUB_KEYS = {"zone", "color", "max_drones"}
COLOR_KEYS = {"red", "green", "yellow", "blue"}


class Map():
    def __init__(self,
                nb_drones,
                start,
                end,
                hub,
                connections):
        self.nb_drones = nb_drones
        self.start = start
        self.end = end
        self.hubs = hubs
        self.connections = connections


class MapGen():
    def __init__(self, path):
        self.path = path
        self.nb: [] = nb
        self.start: [] = start
        self.end: [] = end
        self.hubs: [] = hubs
        self.connections: [] = connections

    def parser(self):
        pos = 0
        with open(path, "r") as f:
            for i, line in enumerate(f):
                if line.startswith("#") or line.startswith("\n"):
                    continue
                if line.startswith("nb_drones:"):
                    set_nbdrones(pos, line, i)
                    p += 1
                elif line.startswith("start_hub:")
                    set_start(pos, line, f"[ERROR] line {i}, <start_hub>")
                elif line.startswith("end_hub:")
                    set_end(pos, line, f"[ERROR] line {i}, <end_hub>")
                elif line.startswith("hub:"):
                    set_hub(pos, line, f"[ERROR] line {i}, <hub>")
                elif line.startswith("connection:")
                    p += 1
                    set_connection(pos, line, f"[ERROR] line {i}, <connection>")
            check_repetition("[ERROR] Repetition error:")
            check_coord("[ERROR] Repetition error:")
            create_map()

    def set_nbdrones(self, p, l, i):
        if p != 0:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> must be declared first")
        n = int(l.split(":")[1])
        self.nb.append(n)
        if len(self.nb) > 1:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> repetition found")
        if n <= 0:
            raise ParseError(f"[ERROR] line {i}, <nb_drones> invalid number of drones")

    def set_start(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:
                             expected order <nb_drones> <hubs> <connections>")
        info = line.split(":")[1]
        info = info.split(" ")
        name = info[0]
        if name.find("-") == -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        x = int(info[1])
        y = int(info[2])
        metadata = h_metadata_parser(info[3], msg)
        start: StartHub = StartHub(name, x, y, metadata) 
        self.start.append(start)
        if len(self.start) > 1:
            raise ParseError(f"{msg} repetition found: expected one start_hub")

    def set_end(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:
                             expected order <nb_drones> <hubs> <connections>")
        info = line.split(":")[1]
        info = info.split(" ")
        name = info[0]
        if name.find("-") == -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        x = int(info[1])
        y = int(info[2])
        metadata = h_metadata_parser(info[3], msg)
        end: EndHub = EndHub(name, x, y, metadata)
        self.end.append(end)
        if len(self.end) > 1:
            raise ParseError(f"{msg} repetition found: expected one <end_hub>")

    def set_hub(self, p, l, msg):
        if p != 1:
            raise ParseError(f"{msg} in wrong position:
                             expected order <nb_drones> <hubs> <connections>")
        info = line.split(":")[1]
        info = info.split(" ")
        name = info[0]
        if name.find("-") != -1:
            raise ParseError(f"{msg} invalid name: '-' are forbidden")
        x = int(info[1])
        y = int(info[2])
        metadata = h_metadata_parser(info[3], msg)
        hub: CommonHub = CommonHub(name, x, y, metadata) 
        self.hubs.append(end)

    def set_connection(self, p, l, msg)
        if p != 2:
            raise ParseError(f"{msg} in wrong position:
                             expected order <nb_drones> <hubs> <connections>")
        info = line.split(":")[1]
        info = info.split(" ")
        name = info[0]
        if name.find("-") == -1:
            raise ParseError(f"{msg} invalid name: expected syntax <name1>-<name2>")
        if len(info) > 1:
            metadata = c_metadata_parse(info[3], msg)
        connection: CommonHub = CommonHub(name, x, y, metadata) 
        self.connections.append(end)

    def h_metadata_parser(self, data, msg):
        parsed = []
        fb = data.find("[")
        sb = data.find("]")
        if fb == -1 or sb == -1:
            raise ParseError(f"{msg} invalid
                                 metadata syntax: expected '[]'")
        if not (data.startswith("[") or data.endswith("]")):
            raise ParseError(f"{msg} invalid
                                 metadata syntax: found data out of brackets")
        data = data.strip("[]")
        data = data.split()
        for x in data:
            k_v = x.split("=")
            if len(k_v) != 2:
                raise ParseError(f"{msg} invalid
                                 metadata syntax: expected <HUB_KEYS>=<VALUE>")
            parsed.append(k_v)
        return parsed

        def c_metadata_parser(self, data, msg):
        parsed = []
        fb = data.find("[")
        sb = data.find("]")
        if fb == -1 or sb == -1:
            raise ParseError(f"{msg} invalid
                                 metadata syntax: expected '[]'")
        if not (data.startswith("[") or data.endswith("]")):
            raise ParseError(f"{msg} invalid
                                 metadata syntax: found data out of brackets")
        data = data.strip("[]")
        k_v = x.split("=")
        if len(k_v) != 2:
            raise ParseError(f"{msg} invalid
                             metadata syntax: expected <CONNECTION_KEYS>=<VALUE>")
        parsed.append(k_v)
        return parsed

    def create_map(self):
        nb = self.nb[0]
        start = self.start[0]
        if start.data:
            start.check_data()
            start.extract_data()
        end = self.end[0]
        if end.data:
            end.check_data()
            end.extract_data()
        for h in hubs:
            if h.data:
                h.check_data()
                h.extract_data()
        for c in connections:
            if c.data:
                c.check_data()
                c.extract_data()
        map = Map(nb, start, end, hubs, connections)

    def check_coord(self, msg):
        seen = ()
        for h in self.hubs:
            if h.x, h.y in seen:
                raise ParseError(f"{msg} found same coords for different hubs")
            else:
                seen.append(h.x, h.y)

    def check_repetition(self, msg):
        seen_s: set = ()
        seen_d: dict = {}
        if self.start[0].x == self.end[0].x
            and self.start[0].y == self.start[0].y:
            raise ParseError(f"{msg} found same coords for start and end")
        for h in self.hubs:
            if h.name in seen_s:
                raise ParseError(f"{msg} found same name {h.name} for hubs")
            else:
                seen_s.append(h.name)
        for c in self.connections:
            if c.name1, c.name2 in seen_d or c.name2, c.name1 in seen_d:
                raise ParseError(f"{msg} found same names
                                 {c.name1}-{c.name2} for connections")
            else:
                seen_d[c.name1] = c.name2