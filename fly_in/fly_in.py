from .errors import MapError
from .hubs import Hub, StartHub, EndHub
from .connections import Connection
from .drones import Drone

def restricted_case(d, c, h, t):
    c.status.append((t, h.add_drone()))
    c.exit_drone()
    d.status.append((t, h))
    h.status.append((t + 1, ( h.add_drone())))
    d.status.append((t + 1, h))
    h.exit_drone()

def drone_scheduler(d, sim, nb_drones):
    t = 0
    st_path = d.space_time_path(nb_drones)
    print(f"=== DRONE{d.id} ===")
    for h in st_path:
        if not (h is StartHub or h is EndHub) and h.t_cost < 2.0:
            h.status.append((t, h.add_drone()))
            h.exit_drone()
        elif h.t_cost == 2.0:
            c = h.get_connection(h.parent)
            restricted_case(d, c, h, t)
            t += 2
            continue
        d.status.append((t, h))
        t += 1
    for t in d.status:
        print(f"turn {t[0]} - hub {t[1].name}")
    sim = d.status

def fly_in(drones):
    simulation = []
    for d in drones:
        d.create_new_path()
        drone_scheduler(d, simulation, len(drones))
    #return simulation