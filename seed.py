import model
import csv
import sys


###CONVERT TIMES (12:00:00) INTO MINUTES OF THE DAY
def get_minutes(time_string):
    time = time_string.split(":")
    time = time[0]*60 + time[1]
    return time

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



###LOAD UP DATA TABLES:


def load_bus_routes():
    #route_id,route_short_name,route_long_name,route_type,route_color,route_text_color,route_url
    f = open("busschedules/routes.txt")
    print f
    routes = f.readlines()
    print routes
    for route in routes:
        route_col = route.split(",")
        new_route = model.BusRoutes(route_id=route_col[0], route_short_name=route_col[1], route_long_name=route_col[2], route_type=route_col[3], route_color=route_col[4], route_text_color=route_col[5], route_url=route_col[6])
        model.session.add(new_route)
    model.session.commit()




def load_bus_stops():
    #stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station,zone_id,wheelchair_boarding
    f = open("busschedules/stops.txt")
    stops = f.readlines()
    for stop in stops:
        stop_col = stop.split(",")
        new_stop = model.BusStops(stop_id=stop_col[0], stop_name=stop_col[1], stop_lat=stop_col[2], stop_lon=stop_col[3], location_type=stop_col[4], parent_station=stop_col[5], zone_id=stop_col[6], wheelchair_boarding=stop_col[7])
        model.session.add(new_stop)
    model.session.commit()



###HUGE####
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



def load_bus_trips():
    #route_id,service_id,trip_id,trip_headsign,block_id,direction_id,shape_id
    f = open("busschedules/trips.txt")
    trips = f.readlines()
    for trip in trips:
        trip_col = trip.split(",")
        new_trip = model.BusTrips(route_id=trip_col[0], service_id=trip_col[1], trip_id=trip_col[2], trip_headsign=trip_col[3], block_id=trip_col[4], direction_id=trip_col[5], shape_id=trip_col[6])
        model.session.add(new_trip)
    model.session.commit()


def load_bus_transfers():
    #from_stop_id,to_stop_id,transfer_type,min_transfer_time
    f = open("busschedules/transfers.txt")
    transfers = f.readlines()
    for transfer in transfers:
        transfer_col = transfer.split(",")
        new_transfer = model.BusTransfers(from_stop_id=transfer_col[0], to_stop_id=transfer_col[1], transfer_type=transfer_col[2], min_transfer_time=transfer_col[3])
        model.session.add(new_transfer)
    model.session.commit()



def load_bus_agency():
    #agency_name,agency_url,agency_timezone,agency_lang,agency_fare_url
    f = open("busschedules/agency.txt")
    agencies = f.readlines()
    for agency in agencies:
        agency_col = agency.split(",")
        new_agency = model.BusAgency(agency_name=agency_col[0], agency_url=agency_col[1], agency_timezone=agency_col[2], agency_lang=agency_col[3], agency_fare_url=agency_col[4])
        model.session.add(new_agency)
    model.session.commit()



def load_bus_fare_attributes():
    #fare_id,price,currency_type,payment_method,transfers,transfer_duration
    f = open("busschedules/fare_attributes.txt")
    fare_attributes = f.readlines()
    for fare_attribute in fare_attributes:
        fare_attribute_col = fare_attribute.split(",")
        new_fare_attribute = model.BusFareAttributes(fare_id=fare_attribute_col[0], price=fare_attribute_col[1], currency_type=fare_attribute_col[2], payment_method=fare_attribute_col[3], transfers=fare_attribute_col[4], transfer_duration=fare_attribute_col[5])
        model.session.add(new_fare_attribute)
    model.session.commit()




def load_bus_fare_rules():
    #fare_id,origin_id,destination_id
    f = open("busschedules/fare_rules.txt")
    fare_rules = f.readlines()
    for fare_rule in fare_rules:
        fare_rule_col = fare_rule.split(",")
        new_fare_rule = model.BusFareRules(fare_id=fare_rule_col[0], origin_id=fare_rule_col[1], destination_id=fare_rule_col[2])
        model.session.add(new_fare_rule)
    model.session.commit()


def load_bus_shapes():
    #shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence
    f = open("busschedules/shapes.txt")
    shapes = f.readlines()
    for shape in shapes:
        shape_col = shape.split(",")
        new_shape = model.BusShapes(shape_id=shape_col[0], shape_pt_lat=shape_col[1], shape_pt_lon=shape_col[2], shape_pt_sequence=shape_col[3])
        model.session.add(new_shape)
    model.session.commit()

#############################



def load_rails_routes():
    #route_id,route_short_name,route_long_name,route_desc,agency_id,route_type,route_color,route_text_color,route_url
    f = open("railschedules/routes.txt")
    routes = f.readlines()
    for route in routes:
        route_col = route.split(",")
        new_route = model.RailsRoutes(route_id=route_col[0], route_short_name=route_col[1], route_long_name=route_col[2], route_desc=route_col[3], agency_id=route_col[4], route_type=route_col[5], route_color=route_col[6], route_text_color=route_col[7], route_url=route_col[8])
        model.session.add(new_route)
    model.session.commit()

def load_rails_stops():
    #stop_id,stop_name, stop_desc, stop_lat, stop_lon, zone_id
    f = open("railschedules/stops.txt")
    stops = f.readlines()
    for stop in stops:
        stop_col = stop.split(",")
        new_stop = model.RailsStops(stop_id=stop_col[0], stop_name=stop_col[1], stop_desc=stop_col[2], stop_lat=stop_col[3], stop_lon=stop_col[4], zone_id=stop_col[5])
        model.session.add(new_stop)
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

def load_rails_trips():
    #route_id,service_id,trip_id,trip_headsign,block_id,trip_short_name,shape_id,direction_id
    f = open("railschedules/trips.txt")
    trips = f.readlines()
    for trip in trips:
        trip_col = trip.split(",")
        new_trip = model.RailsTrips(route_id=trip_col[0], service_id=trip_col[1], trip_id=trip_col[2], trip_headsign=trip_col[3], block_id=trip_col[4], trip_short_name=trip_col[5], shape_id=trip_col[6], direction_id=trip_col[7])
        model.session.add(new_trip)
    model.session.commit()

def load_rails_transfers():
    #from_stop_id,to_stop_id,transfer_type
    f = open("railschedules/transfers.txt")
    transfers = f.readlines()
    for transfer in transfers:
        transfer_col = transfer.split(",")
        new_transfer = model.RailsTransfers(from_stop_id=transfer_col[0], to_stop_id=transfer_col[1], transfer_type=transfer_col[2])
        model.session.add(new_transfer)
    model.session.commit()


def load_rails_agency():
    #agency_id, agency_name, agency_url, agency_timezone, agency_lang
    f = open("railschedules/agency.txt")
    agencies = f.readlines()
    for agency in agencies:
        agency_col = agency.split(",")
        new_agency = model.RailsAgency(agency_id=agency_col[0], agency_name=agency_col[1], agency_url=agency_col[2], agency_timezone=agency_col[3], agency_lang=agency_col[4])
        model.session.add(new_agency)
    model.session.commit()



def load_rails_shapes():
    #shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence
    f = open("railschedules/shapes.txt")
    shapes = f.readlines()
    for shape in shapes:
        shape_col = shape.split(",")
        new_shape = model.RailsShapes(shape_id=shape_col[0], shape_pt_lat=shape_col[1], shape_pt_lon=shape_col[2], shape_pt_sequence=shape_col[3])
        model.session.add(new_shape)
    model.session.commit()


# def main(session):
#     pass


# if __name__ == "__main__":
#     main(s)


