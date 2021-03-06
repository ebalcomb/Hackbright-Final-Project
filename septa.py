import requests
import model


## THIS FILE FUNCTIONS AS A PYTHON API FOR SEPTA ##

#CLASSES

class Location(object):
    def __init__(self, json_obj):
        self.id = json_obj['location_id']
        self.name = json_obj['location_name']
        self.lat = float(json_obj['location_lat'])
        self.lon = float(json_obj['location_lon'])
        self.distance = float(json_obj['distance'])
        self.location_type = json_obj['location_type']


class Elevator(object):
    def __init__(self, json_obj):
        self.line = json_obj['line']
        self.station = json_obj['station']
        self.elevator = json_obj['elevator']
        self.message = json_obj['message']
        self.alternate_url = json_obj['alternate_url']

class NextTrain(object):
    def __init__(self, json_obj):
        self.orig_train = json_obj['orig_train']
        self.orig_line = json_obj['orig_line']
        self.departure_time = json_obj['departure_time']
        self.arrival_time = json_obj['arrival_time']
        self.orig_delay = json_obj['orig_delay']
        self.isdirect = json_obj['isdirect']


class BusLocation(object):
    def __init__(self, json_obj):
        self.lat = json_obj['self']
        self.lng = json_obj['lng']
        self.label = json_obj['label']
        self.VehicleID = json_obj['VehicleID']
        self.Direction = json_obj['Direction']
        self.destination = json_obj['destination']
        self.Offset = json_obj['Offset']

# class Route(object):
#     def __init__(self, json_obj):
#         self.route_id = json_obj['route_id']
#         self.route_name = json_obj['route_name']
#         self.current_message = json_obj['current_message']
#         self.advisory_message = json_obj['advisory_message']
#         self.detour_message = json_obj['detour_message']
#         self.detour_start_location = json_obj['detour_start_location']
#         self.detour_start_date_time = json_obj['detour_start_date_time']
#         self.detour_end_date_time = json_obj['detour_end_date_time']
#         self.detour_reason = json_obj['detour_reason']
#         self.last_updated = json_obj['last_updated']

class Route:
    def __init__(self, route_id, route_name, route_type):
        self.id = route_id
        self.route_name = route_name
        self.type = route_type


class Stop:
    def __init__(self, stop_id, stop_name):
        self.id = stop_id
        self.name = stop_name
        self.paths = []


class Path:
    def __init__(self, start, end, distance):
        self.start_stop = start
        self.end_stop = end
        self.distance = distance

class Trip:
    def __init__(self, trip_id, route_id, veh_type):
        self.id = trip_id
        self.route_id = route_id
        self.veh_type = veh_type

class StopTimes:
    def __init__(self, stop_id, trip_id, stop_time):
        self.stop_id = stop_id
        self.trip_id = trip_id
        self.stop_time = stop_time



#FUNCTIONS TO EXTRACT SEPTA DATA


#get_nearby_locations
#uses latitude, longitude, and radius of starting location
#result is a list of objects of the "Location" class
def get_nearby_locations(lon, lat, radius):
    #example coords: lon: -75 lat: 40
    url = "http://www3.septa.org/hackathon/locations/get_locations.php?lon=%f&lat=%f&radius=%f"
    response = requests.get(url%(lon, lat, radius))
    data = response.json()
    nearby_locations = []

    for item in data:
        nearby_locations.append(item["location_id"])

    print "nearby locations", nearby_locations
    
    closest_stop = model.access_check(nearby_locations)
    return closest_stop



#get_elevator_outages
#result is a list of elevators that are out of service 
#result is a list of objects of the "Elevator" class
def get_elevator_outages():
    url = "http://www3.septa.org/hackathon/elevator/"
    response = requests.get(url)
    data = response.json()
    broken_elevators = []

    for item in data["results"]:
        elev = Elevator(item)
        broken_elevators.append(elev)
    return broken_elevators



#next_to_arrive
#REGIONAL RAIL ONLY
#takes start station, end station, number of results
#result is a list of objects of the NextTrain class
def next_to_arrive(start_station, end_station, results):
    url = "http://www3.septa.org/hackathon/NextToArrive/%s/%s/%s" %(start_station, end_station, results)
    response = requests.get(url)
    data = response.json()
    next_trains = []

    for item in data:
        next = NextTrain(item)
        next_trains.append(next)
    return next_trains



# SCHEDULES

# STOPS AND STOP ACCESSIBILITY

# REAL TIME BUS/TRAIN LOCATIONS

# DELAY INFORMATION