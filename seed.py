import model
import csv
import sys
import algorithm


###CONVERT TIMES (12:00:00) INTO MINUTES OF THE DAY
def get_minutes(time_string):
    time = time_string.split(":")
    minutes = int(time[0])*60 + int(time[1])
    return minutes

###CONVERTS MINUTES OF THE DAY INTO TIME (12:00:00)
def get_time(minutes):
    hour = str(minutes/60)
    minute = str(minutes % 60)
    if len(hour) != 2:
        hour = "0%s" % hour
    if len(minute) != 2:
        minute = "0%s" % minute
    time = "%s:%s:00" % (hour, minute)
    return time



##################################
# STOPS
##################################

accessible_bus_stops = []
def load_bus_stops():
    #stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station,zone_id,wheelchair_boarding
    f = open("busschedules/stops.txt")
    stops = f.readlines()
    for stop in stops:
        stop_col = stop.split(",")
        if stop_col[7].strip() != "0" and stop_col[7].strip() != 0:
            new_stop = model.Stops(id=stop_col[0], stop_name=stop_col[1], stop_lat=stop_col[2], stop_lon=stop_col[3], stop_type = "bus")
            model.session.add(new_stop)
            accessible_bus_stops.append(int(stop_col[0]))
    model.session.commit()
    return accessible_bus_stops


def load_rails_stops():
    #stop_id,stop_name, stop_desc, stop_lat, stop_lon, zone_id
    g = open("railschedules/accessiblerailsstops")
    stops = g.readlines()
    accessible_stop_ids = []
    for stop in stops:
        stop.strip()
        accessible_stop_ids.append(int(stop))
    f = open("railschedules/stops.txt")
    rail_stops = f.readlines()
    for stop in rail_stops:
        stop = stop.split(",")
        stop_id = stop[0].strip()
        if int(stop_id) in accessible_stop_ids:
            new_stop = model.Stops(id=stop[0], stop_name=stop[1], stop_lat=stop[3], stop_lon=stop[4], stop_type = "rail")
            model.session.add(new_stop)
    model.session.commit()


def load_subway_stops():
    f = open("subwayschedules/stops.csv")
    stops = f.readlines()
    accessible_bus_stops = load_bus_stops()
    for stop in stops:
        stop = stop.split(",")
        if int(stop[1]) not in accessible_bus_stops:
            new_stop = model.Stops(id=int(stop[1]), stop_name=stop[2], stop_lat=0, stop_lon=0, stop_type = "subway")
            model.session.add(new_stop)
    model.session.commit()

##################################
# ROUTES
##################################

def load_bus_routes():
    #route_id,route_short_name,route_long_name,route_type,route_color,route_text_color,route_url
    f = open("busschedules/routes.txt")
    routes = f.readlines()
    for route in routes:
        route_col = route.split(",")
        new_route = model.Routes(id=route_col[0], route_short_name=route_col[1], route_long_name=route_col[2], route_type="bus")
        model.session.add(new_route)
    model.session.commit()


def load_rails_routes():
    #route_id,route_short_name,route_long_name,route_desc,agency_id,route_type,route_color,route_text_color,route_url
    f = open("railschedules/routes.txt")
    routes = f.readlines()
    for route in routes:
        route_col = route.split(",")
        new_route = model.Routes(route_short_name=route_col[1], route_long_name=route_col[2], route_type="rail")
        model.session.add(new_route)
    model.session.commit()

def load_subway_routes():
    f = open("subwayschedules/routes.csv")
    routes = f.readlines()
    for route in routes:
        route_col = route.split(",")
        new_route = model.Routes(route_short_name=route_col[1], route_long_name=route_col[1], route_type="subway")
        model.session.add(new_route)
    model.session.commit()



##################################
# TRIPS
##################################

def load_bus_trips():
    #route_id,service_id,trip_id,trip_headsign,block_id,direction_id,shape_id
    f = open("busschedules/trips.txt")
    covered_routes = []
    covered_trips = []
    trips = f.readlines()
    for trip in trips:
        trip_col = trip.split(",")
        if int(trip_col[0]) not in covered_routes:
            new_trip = model.Trips(id=trip_col[2], trip_id=trip_col[2], route_id=trip_col[0], direction_id=trip_col[5])
            model.session.add(new_trip)
            covered_routes.append(int(trip_col[0]))
            covered_trips.append(int(trip_col[2]))
    model.session.commit()
    for trip in covered_trips:
        print trip


def load_rails_trips():
    #route_id,service_id,trip_id,trip_headsign,block_id,trip_short_name,shape_id,direction_id
    f = open("railschedules/trips.txt")
    covered_routes = []
    covered_trips = []
    trips = f.readlines()
    for trip in trips:
        trip_col = trip.split(",")
        if (trip_col[0]) not in covered_routes:
            new_trip = model.Trips(trip_id=trip_col[2], route_id=trip_col[0], direction_id=trip_col[5])
            model.session.add(new_trip)
            covered_routes.append(trip_col[0])
            covered_trips.append(trip_col[2])
    model.session.commit()
    for trip in covered_trips:
        print trip


##################################
# STOP TIMES
##################################

def load_bus_stop_times():
    #trip_id,arrival_time,departure_time,stop_id,stop_sequence
    f = open("busschedules/stop_times.txt")
    stop_times = f.readlines()
    for stop_time in stop_times:
        stop_time_col = stop_time.split(",")
        arrival_time = get_minutes(stop_time_col[1])
        new_stop_time = model.StopTimes(trip_id=stop_time_col[0], arrival_time=stop_time_col[1], stop_id=stop_time_col[3])
        model.session.add(new_stop_time)
    model.session.commit()

def load_rails_stop_times():
    #trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type
    f = open("railschedules/stop_times.txt")
    stop_times = f.readlines()
    for stop_time in stop_times:
        stop_time_col = stop_time.split(",")
        arrival_time = get_minutes(stop_time_col[1])
        new_stop_time = model.StopTimes(trip_id=stop_time_col[0], arrival_time=stop_time_col[1], stop_id=stop_time_col[3])
        model.session.add(new_stop_time)
    model.session.commit()



##################################
# PATHS
##################################

def load_bus_paths():
    f = open("busschedules/interesting_times.txt")
    stop_times = f.readlines()
    for i in range(len(stop_times)-1):
        stop_col1 = stop_times[i].split(",")
        stop_col2 = stop_times[i+1].split(",")
        if stop_col1[0] == stop_col2[0]:
            start_stop = stop_col1[3]
            end_stop = stop_col2[3]
            #start_time = stop_times[i+1][1]
            #end_time = stop_times[i][1]
            #print "START TIME: ", start_time
            #print "END TIME: ", end_time
            #cost = get_minutes(stop_times[i+1][1]) - get_minutes(stop_times[i][1])
            new_path = model.Paths(start_stop=int(start_stop), end_stop=int(end_stop), cost=5)
            model.session.add(new_path)
    model.session.commit()


def load_intrapaths():
    f = open("intrapaths.csv")
    paths = f.readlines()
    for path in paths:
        path = path.split(",")
        new_path = model.Paths(start_stop=path[0], end_stop=path[1], cost=5)
        model.session.add(new_path)
    model.session.commit()


def load_interpaths():
    f = open("interpaths.csv")
    paths = f.readlines()
    for path in paths:
        path = path.split(",")
        new_path = model.Paths(start_stop=path[0], end_stop=path[1], cost=5)
        model.session.add(new_path)
    model.session.commit()

def load_shortest_routes():
    start_stops = model.get_stops()
    end_stops = model.get_stops()

    for start_stop in start_stops:
        for end_stop in end_stops:
            start = int(start_stop.id)
            end = int(end_stop.id)
            shortest_route = algorithm.find_route(start, end)
            if shortest_route:
                route_string = str(shortest_route).strip('[]')
                new_shortest_route = model.ShortestRoute(start_stop=start_stop, end_stop=end_stop, stops_hit=route_string)
                model.session.add(new_shortest_route)
    model.session.commit()



def main():
    load_rails_stops()
    load_subway_stops()
    load_bus_routes()
    load_rails_routes()
    load_subway_routes()
    load_bus_trips()
    load_rails_trips()
    load_bus_stop_times()
    load_rails_stop_times()
    load_interpaths()


