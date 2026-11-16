from .drones import Drone
from .map import Map

def let_em_fly(m, drones):
    turn = 0
    while not stop_fleet(m):
        for d in m.drones:
            new_path = d.get_new_path()
            best_path(d)
            h = best_path[0]
            if not h.available and h.t_cost == 2.0:
                if not recalculate_path(d):
                    d.pos = h.connection
                    h.connection.add_drone()
                    continue
            elif not h.available:
                if not recalculate_path(d):
                    continue
        turn += 1

def stop_fleet(m):
    for d in m.drones:
        if not d.has_landed():
            return False
    return True

def best_path(d):
    path_moves = {}
    for p in d.path:
        moves = calculate_moves(p)
        path_moves[moves] = p
    lowest = path.moves.get(min(path.moves.keys()))
    d.path.clear()
    d.path.append(lowest)

def calculate_moves(path):
    count = 0
    for h in path:
        if not h.is_available:
            count += 1
        if h.t_cost <= 1.0:
            count += 1
        elif h.t_cost == 2.0:
            count += 2
    return count
