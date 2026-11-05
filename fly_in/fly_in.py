from .drones import Drone
from .map import Map

def let_em_fly(map, drones):
    turn = 0
    while not stop_fleet(map):
        for d in map.drones:
            new_path = d.get_new_path()
            best_path(d)
            for h in d.path():
                if not h.available or h.:

                d.pos = h

def stop_fleet(map):
    for d in map.drones:
        if not d.has_landed():
            return False
    return True

def best_path(d):
    path_moves = {}
    for p in d.path:
        moves = calculate_moves(p)
        path_moves(p) = moves
    lowest = path.moves.get(min(path.moves.values()))
    d.path.clear()
    d.path.append(lowest)

def calculate_moves(path):
    count = 0
    for h in path:
        count += 1
        if not h.is_available:
            count += 1
        if h.t_cost <= 1.0:
            count += 1
        elif h.t_cost == 2.0:
            count += 2
    return count

def recalculate_path(d):
    old = d.path
    if 