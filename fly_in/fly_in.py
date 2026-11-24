from .errors import MapError
from .hubs import Hub, StartHub, EndHub
from .connections import Connection
from .drones import Drone


def fly_in(drones):
    for d in drones:
        d.create_new_path()
        d.set_status()
        d.booking_hub()
    #return simulation