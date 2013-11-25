#Goal: use Dijkstra's algorthim to find shortest leg between 2 stops
import model

class Map(object):
    def __init__(self, stops, paths):
        self.stops = stops
        self.paths = paths

    
    def add_stop(self, stop_id):
        new_stop = Stop(stop_id)
        self.stops.add(new_stop)
    
    def add_path(self, from_stop, to_stop, distance):
        new_path = Path(from_stop, to_stop, distance)
        new_return_path = Path(to_stop, from_stop, distance)
        self.paths.add(new_path)
        self.paths.add(new_return_path)


class Stop:
    def __init__(self, stop_id):
        self.id = stop_id
        self.paths = []


class Path:
    def __init__(self, start, end, distance):
        self.start_stop = start
        self.end_stop = end
        self.distance = distance


def create_map_from_DB():
    db_paths = model.get_paths()
    stops = {}
    paths = []
    for path in db_paths:

        start_stop = path.start_stop
        end_stop = path.end_stop
        cost = path.cost

        if start_stop not in stops:
            start = Stop(path.start_stop)
            stops[start.id] = start
        else:
            start = stops[start_stop]

        if end_stop not in stops:
            end = Stop(end_stop)
            stops[end.id] = end
        else:
            end = stops[end_stop]

        path = Path(start, end, cost)
        start.paths.append(path)

        return_path = Path(end, start, cost)
        end.paths.append(return_path)

        paths.append(path)

    new_map = Map(stops, paths)
    return new_map


def create_map(csv):
    f = open(csv)
    r = f.readlines()
    rows = []
    for row in r:
        row = row.strip()
        row = row.split(",")
        final_row = []
        for item in row: 
            item = int(item)
            final_row.append(item)
        rows.append(final_row)


    stops = {}
    paths = []
    for row in rows:

        if row[1] not in stops:
            start = Stop(row[1])
            stops[start.id] = start
        else:
            start = stops[row[1]]

        if row[2] not in stops:
            end = Stop(row[2])
            stops[end.id] = end
        else:
            end = stops[row[2]]

        distance = row[3]

        path = Path(start, end, distance)
        start.paths.append(path)

        return_path = Path(end, start, distance)
        end.paths.append(return_path)

        paths.append(path)

    new_map = Map(stops, paths)
    return new_map

my_map = create_map_from_DB()

def shortest_route(graph, initial_stop, goal_stop):
    distances, routes = dijkstra(graph, initial_stop)
    route = [goal_stop]
 
    while goal_stop != initial_stop:
        route.append(routes[goal_stop])
        goal_stop = routes[goal_stop]
 
    route.reverse()
    return route 

def find_route(initial_stop, goal_stop):
    route = shortest_route(my_map, initial_stop, goal_stop)
    if route:
        return route
    else:
        return False


def dijkstra(graph, initial_stop):
    visited = {initial_stop: 0}

    route = {}
    stops = []

    for stop in graph.stops:
        stops.append(stop)
    stops = set(stops)

    
    while stops:
        min_stop = None
        for stop in stops:
            if stop in visited:
                if min_stop is None:
                    min_stop = graph.stops[stop]
                elif visited[stop] < visited[min_stop.id]:
                    min_stop = graph.stops[stop]
 
        if min_stop is None:
            break
 
        stops.remove(min_stop.id)
        cur_wt = visited[min_stop.id]


        for path in min_stop.paths:
            wt = cur_wt + path.distance
            if path.end_stop.id not in visited or wt < visited[path.end_stop.id]:
                visited[path.end_stop.id] = wt
                route[path.end_stop.id] = min_stop.id

    return visited, route




#TESTING

sample_map = create_map("sample.csv")

def test_integrity():
    assert shortest_route(sample_map, 1, 5) == [1, 3, 2, 5]
    assert shortest_route(sample_map, 5, 1) == [5, 2, 3, 1]
    assert shortest_route(sample_map, 2, 5) == [2, 5]
    assert shortest_route(sample_map, 3, 5) == [3, 2, 5]