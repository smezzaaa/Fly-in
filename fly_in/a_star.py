from .errors import ParseError
from .hubs import Hub, EndHub, StartHub

def get_distance(a: Hub, b: Hub) -> int:
    ax = a.coord[0]
    bx = b.coord[0]
    ay = a.coord[1]
    by = b.coord[1]
    dst_x: int = abs(ax - bx)
    dst_y: int = abs(ay - by)
    return (dst_x + dst_y)


def retrace_path(start: Hub, end: Hub) -> list[Hub]:
    path: list[Hub] = []
    curr: Hub = end
    while curr != start:
        curr.path = True
        path.append(curr)
        curr = curr.parent  # type: ignore
    path.append(curr)
    path.reverse()
    return(path)


def a_star(start: StartHub, end: EndHub, id: int) -> list[Hub]:
    logged: list[Hub] = []
    seen: list[Hub] = []
    logged.append(start)
    t = 0
    while (len(logged) > 0):
        curr: Hub = logged[0]
        for x in logged:
            if (x.get_cost() < curr.get_cost()) or \
                    ((x.get_cost() == curr.get_cost())
                        and (x.h_cost < curr.h_cost)):
                curr = x
        logged.remove(curr)
        seen.append(curr)
        if (curr == end):
            return(retrace_path(start, end))
        neighbours: list[Hub] = curr.n_hubs
        for n in neighbours:
            if n in seen or n.is_full_at(t + 1):
                continue
            temp_path = curr.g_cost + 1
            if n not in logged or (temp_path < n.g_cost):
                n.g_cost = temp_path
                n.h_cost = get_distance(n, end)
                n.parent = curr  # type: ignore
                if n not in logged:
                    logged.append(n)
        t += 1
    return(seen)