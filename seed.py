import model
import csv
import sys


###CONVERT TIMES (12:00:00) INTO MINUTES OF THE DAY
def get_minutes(time_string):
    time = time_string.split(":")
    print "TIME:::::::::::", time
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


def load_rails_stops():
    #stop_id,stop_name, stop_desc, stop_lat, stop_lon, zone_id
    g = open("accessiblerailsstops")
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
    for stop in stops:
        stop = stop.split(",")
        new_stop = model.Stops(id=int(stop[1]), stop_name=stop[2], stop_lat=0, stop_lon=0, stop_type = "subway")
        model.session.add(new_stop)
    model.session.commit()

##################################
# ROUTES
##################################

def load_bus_routes():
    #route_id,route_short_name,route_long_name,route_type,route_color,route_text_color,route_url
    f = open("busschedules/routes.txt")
    print f
    routes = f.readlines()
    print routes
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
        departure_time = get_minutes(stop_time_col[2])
        new_stop_time = model.BusStopTimes(trip_id=stop_time_col[0], arrival_time=arrival_time, departure_time=departure_time, stop_id=stop_time_col[3], stop_sequence=stop_time_col[4])
        model.session.add(new_stop_time)
    model.session.commit()

def load_rails_stop_times():
    #trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type
    f = open("railschedules/stop_times.txt")
    stop_times = f.readlines()
    for stop_time in stop_times:
        stop_time_col = stop_time.split(",")
        arrival_time = get_minutes(stop_time_col[1])
        departure_time = get_minutes(stop_time_col[2])
        new_stop_time = model.RailsStopTimes(trip_id=stop_time_col[0], arrival_time=arrival_time, departure_time=departure_time, stop_id=stop_time_col[3], stop_sequence=stop_time_col[4], pickup_type=stop_time_col[5], drop_off_type=stop_time_col[6])
        model.session.add(new_stop_time)
    model.session.commit()



##################################
# PATHS
##################################

def load_bus_paths():
    f = open("busschedules/interesting_times.txt")
    stop_times = f.readlines()
    for i in range(len(stop_times)-1):
        if stop_times[i][0] == stop_times[i+1][0]:
            print "stop time[i]: ", stop_times[i]
            start_stop = stop_times[i][3]
            end_stop = stop_times[i+1][3]
            start_time = stop_times[i+1][1]
            end_time = stop_times[i][1]
            print "START TIME: ", start_time
            print "END TIME: ", end_time
            cost = get_minutes(stop_times[i+1][1]) - get_minutes(stop_times[i][1])
            new_path = model.Paths(start_stop=int(start_stop), end_stop=int(end_stop), cost=int(cost))
            model.session.add(new_path)
    model.session.commit()





def load_rails_paths():
    pass



def load_subway_paths():
    pass 



