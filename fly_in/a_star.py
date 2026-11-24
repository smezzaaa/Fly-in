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


def retrace_path(parents, end: tuple[Hub, int]) -> list[Hub]:
    path: list[(Hub, tuple)] = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()
    return path


def calculate_t(n, curr_t, curr):
    if n.zone == "restricted" and curr is not n:
        return curr_t + 2
    else:
        return curr_t + 1


def is_waiting(n, curr):
    return n == curr


def a_star(start: StartHub, end: EndHub, d) -> list[Hub]:
    #print("=== NEIGHBOURS ===")
    logged: list[tuple] = []
    seen: set[tuple] = set()
    g_costs = {(start, 0): 0}
    parents: dict(tuple, tuple) = {(start, 0): None}
    logged.append((start, 0))
    start.h_cost = get_distance(start, end)

    while logged:
        curr = logged[0]
        for x in logged:
            x_cost = x[0].get_cost(g_costs, x[1])
            curr_cost = curr[0].get_cost(g_costs, curr[1])
            if (x_cost < curr_cost) or \
                ((x_cost == curr_cost) and (x[0].h_cost < curr[0].h_cost)):
                curr = x
        logged.remove(curr)
        seen.add(curr)
        if (curr[0] == end):
            return retrace_path(parents, curr)
        neighbours = curr[0].n_hubs.copy()
        #for n in neighbours:
        #    print(f"{curr[0].name} neighbour -> {n.name}")
        neighbours.add(curr[0])
        for n in neighbours:
            next_t = calculate_t(n, curr[1], curr[0])
            next_state = (n, next_t)
            if next_state in seen:
                continue
            if n.zone == "restricted" and n is not curr[0]:
                connection = n.get_connection(curr[0])
                if connection.is_full_at(curr[1] + 1) or n.is_full_at(next_t):
                    parents[(curr[0], next_t - 1)] = curr
                    parents[(curr[0], next_t)] = curr
                    continue
            else:
                #print(f"{n.name} is full at {next_t} = {n.is_full_at(next_t)}")
                if n.is_full_at(next_t):
                    next_state = (curr[0], next_t)
                    parents[next_state] = curr
                    continue

            move_cost = next_t - curr[1]
            temp_path = g_costs[curr] + move_cost
            previous_cost = g_costs.get(next_state, float("inf"))
            if temp_path < previous_cost:
                g_costs[next_state] = temp_path
                n.h_cost = get_distance(n, end)
                if n.zone == "restricted":
                    parents[(n, next_t - 1)] = curr
                parents[next_state] = curr
                if next_state not in logged:
                    logged.append(next_state)
    return []