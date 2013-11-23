#Goal: use Dijkstra's algorthim to find shortest leg between 2 stops

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


    #find cost of path based on current time
    def cost():
        pass



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

        if row[0] not in stops:
            start = Stop(row[0])
            stops[start.id] = start
        else:
            start = stops[row[0]]

        if row[1] not in stops:
            end = Stop(row[1])
            stops[end.id] = end
        else:
            end = stops[row[1]]

        distance = row[2]

        path = Path(start, end, distance)
        start.paths.append(path)

        return_path = Path(end, start, distance)
        end.paths.append(return_path)

        paths.append(path)

    new_map = Map(stops, paths)
    return new_map


def shortest_route(graph, initial_stop, goal_stop):
    distances, routes = dijkstra(graph, initial_stop)
    route = [goal_stop]
 
    while goal_stop != initial_stop:
        route.append(routes[goal_stop])
        goal_stop = routes[goal_stop]
 
    route.reverse()
    return route 

def find_route(initial_stop, goal_stop):
    graph = create_map("interpaths.csv")
    route = shortest_route(graph, initial_stop, goal_stop)
    return route

def route_words(paths, names, initial_stop, goal_stop):
    graph = create_map(paths)
    route = shortest_route(graph, initial_stop, goal_stop)
    f = open(names)
    r = f.readlines()
    id_names = {}
    for row in r:
        row = row.strip()
        row = row.split(",")
        id_names[int(row[1])] = (row[2])
    names = []
    for stop in route:
        names.append(id_names[stop])
    print "to get from %s to %s take the following route:" %(names[0], names[-1])
    for name in names:
        print name 





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

# #Goal: use Dijkstra's algorthim to find shortest leg between 2 stops

# class Map(object):
#     def __init__(self, stops, paths, distances):
#         self.stops = stops
#         self.paths = paths
#         self.distances = distances
    
#     def add_stop(self, value):
#         self.stops.add(value)
    
#     def add_path(self, from_stop, to_stop, distance):
#         self._add_path(from_stop, to_stop, distance)
#         self._add_path(to_stop, from_stop, distance)
 
#     def _add_path(self, from_stop, to_stop, distance):
#         self.paths.setdefault(from_stop, [])
#         self.paths[from_stop].append(to_stop)
#         self.distances[(from_stop, to_stop)] = distance


# def shortest_route(graph, initial_stop, goal_stop):
#     distances, routes = dijkstra(graph, initial_stop)
#     route = [goal_stop]
 
#     while goal_stop != initial_stop:
#         route.append(routes[goal_stop])
#         goal_stop = routes[goal_stop]
 
#     route.reverse()
#     return route 


# def dijkstra(graph, initial_stop):
#     visited = {initial_stop: 0}
#     current_stop = initial_stop
#     route = {}
    
#     stops = set(graph.stops)
#     print "stops: ", stops
    
#     #visited is a list of stops that have been visited. It starts off only having the start node in it, which takes 0 steps to reach, so visited[start] = 0.

#     #while there are stops to search through, we go through and check for the min_stop, which is the stop it takes the fewest steps to get to. 
#     while stops:
#         min_stop = None
#         for stop in stops:
#             if stop in visited:
#                 print "stop: ", stop, "is in visited: ", visited
#                 if min_stop is None:
#                     print "setting min_stop to stop"
#                     min_stop = stop
#                     print "min_stop is now: ", min_stop
#                 elif visited[stop] < visited[min_stop]:
#                     print "setting min_stop to stop (2)"
#                     min_stop = stop
#                     print "min_stop is now: ", min_stop
#             else:
#                 print "stop: ", stop, "is NOT in visited: ", visited
 
#         if min_stop is None:
#             print "breaking"
#             break
        
#         print "min_stop is: ", min_stop
#         print "removing min_stop from stops...."
#         stops.remove(min_stop)
#         print "stops is now: ", stops
#         print "setting cur_wt = visited[min_stop"
#         cur_wt = visited[min_stop]
#         print "cur_wt: ", cur_wt
        

#         print "finding all paths associated with the min_stop"
#         print "graph.paths[min_stop]: ", graph.paths[min_stop]
#         for path in graph.paths[min_stop]:
#             print "checking this path: ", path
#             print "cur_wt: ", cur_wt
#             print "graph.distances[(min_stop, path)]: ", graph.distances[(min_stop, path)]
#             print "adding the new distance between the start point and the new path node to the cur_wt"
#             wt = cur_wt + graph.distances[(min_stop, path)]
#             print "wt: ", wt

#             "checking to see if the path: ", path, "is in visited: ", visited
#             if path not in visited or wt < visited[path]:
#                 print "the path: ", path, "is not in visited: ", visited
#                 print "adding the path: ", path, "to visited: ", visited
#                 visited[path] = wt
#                 print "visited is now: ", visited
#                 print "adding the path: ", path, " to the route: ", route
#                 route[path] = min_stop
#                 print "route is now: ", route
    
#     return visited, route


# def create_map(csv):
#     f = open(csv)
#     r = f.readlines()
#     rows = []
#     for row in r:
#         row = row.strip()
#         row = row.split(",")
#         final_row = []
#         for item in row: 
#             item = int(item)
#             final_row.append(item)
#         rows.append(final_row)


#     stops = []
#     for row in rows:
#         if row[0] not in stops:
#             stops.append(row[0])
#         if (row[1]) not in stops:
#             stops.append(row[1])
#     print "stops: ", stops

#     paths = {}
#     for stop in stops:
#         paths[stop] = []
#     for row in rows:
#         paths[row[0]].extend([row[1]])
#         #only need the row below if the csv does not include transit info in both directions(A>B is a different row than B>A)
#         #paths[row[1]].extend([row[0]])
#     print "paths", paths

#     distances = {}
#     for row in rows:
#         distances[row[0], row[1]] = row[2]
#     print "distances", distances

#     my_map = Map(paths=paths, stops=stops, distances=distances)
#     return my_map




# #TESTING

# sample_map = Map(paths= {1: [2, 4, 3], 2: [1, 5, 3], 3: [1, 2, 4, 5], 4:[5, 1, 3], 5: [2, 4, 3]}, stops = set(range(1,6)), distances = {(1, 2): 3, (2, 5): 4, (5, 4): 4, (4, 1): 3, (1, 3): 1, (2, 3): 1, (5, 3): 6, (4, 3): 2, (2, 1): 3, (5, 2): 4, (4, 5): 4, (1, 4): 3, (3, 1): 1, (3, 2): 1, (3, 5): 6, (3, 4): 2})



# def test_integrity():
#     assert shortest_route(sample_map, 1, 5) == [1, 2, 5]
#     assert shortest_route(sample_map, 5, 1) == [5, 2, 1]
#     assert shortest_route(sample_map, 2, 5) == [2, 5]
#     assert shortest_route(sample_map, 3, 5) == [3, 2, 5]