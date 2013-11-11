#Goal: use Dijkstra's algorthim to find shortest leg between 2 stops

class Map(object):
    def __init__(self, stops, paths, distances):
        self.stops = stops
        self.paths = paths
        self.distances = distances
    
    def add_stop(self, value):
        self.stops.add(value)
    
    def add_path(self, from_stop, to_stop, distance):
        self._add_path(from_stop, to_stop, distance)
        self._add_path(to_stop, from_stop, distance)
 
    def _add_path(self, from_stop, to_stop, distance):
        self.paths.setdefault(from_stop, [])
        self.paths[from_stop].append(to_stop)
        self.distances[(from_stop, to_stop)] = distance


def shortest_route(graph, initial_stop, goal_stop):
    distances, routes = dijkstra(graph, initial_stop)
    route = [goal_stop]
 
    while goal_stop != initial_stop:
        route.append(routes[goal_stop])
        goal_stop = routes[goal_stop]
 
    route.reverse()
    return route 


def dijkstra(graph, initial_stop):
    visited = {initial_stop: 0}
    current_stop = initial_stop
    route = {}
    
    stops = set(graph.stops)
    
    while stops:
        min_stop = None
        for stop in stops:
            if stop in visited:
                if min_stop is None:
                    min_stop = stop
                elif visited[stop] < visited[min_stop]:
                    min_stop = stop
 
        if min_stop is None:
            break
 
        stops.remove(min_stop)
        cur_wt = visited[min_stop]
        
        for path in graph.paths[min_stop]:
            wt = cur_wt + graph.distances[(min_stop, path)]
            if path not in visited or wt < visited[path]:
                visited[path] = wt
                route[path] = min_stop
    
    return visited, route


def dijkstra_words(graph, initial_stop):
	visited, route = dijkstra(graph, initial_stop)
	for item in visited:
		if item in route:
			transfers = route[item] - 1
			print "*** stop", initial_stop,  "> stop", item, ":", visited[item], "minutes of travel,", transfers, " transfers"
	return visited, route


def populate_graph():
	pass


sample_map = Map(paths= {1: [2, 4, 3], 2: [1, 5, 3], 3: [1, 2, 4, 5], 4:[5, 1, 3], 5: [2, 4, 3]}, stops = set(range(1,6)), distances = {(1, 2): 2, (5, 4): 4, (1, 3): 1, (4, 5): 4, (4, 1): 3, (3, 1): 1, (3, 2): 1, (2, 1): 2, (2, 3): 1, (1, 4): 3, (4, 3): 2, (3, 4): 2, (2, 5): 3, (3, 5): 6, (5, 2): 3, (5, 3): 6})



def test_integrity():
    assert shortest_route(sample_map, 1, 5) == [1, 2, 5]
    assert shortest_route(sample_map, 5, 1) == [5, 2, 1]
    assert shortest_route(sample_map, 2, 5) == [2, 5]
    assert shortest_route(sample_map, 3, 5) == [3, 2, 5]