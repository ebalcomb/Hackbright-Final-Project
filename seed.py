import model
import csv
import sys

def load_bus_routes(session):
    pass
    #route_id,route_short_name,route_long_name,route_type,route_color,route_text_color,route_url


def load_bus_stops(session):
    pass
    #stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station,zone_id,wheelchair_boarding

def load_bus_stop_times(session):
    pass
    #trip_id,arrival_time,departure_time,stop_id,stop_sequence

def load_bus_trips(session):
    pass
    #route_id,service_id,trip_id,trip_headsign,block_id,direction_id,shape_id

def load_bus_transfers(session):
    pass
    #from_stop_id,to_stop_id,transfer_type,min_transfer_time

def load_bus_agency(session):
    pass
    #agency_name,agency_url,agency_timezone,agency_lang,agency_fare_url

def load_bus_fare_attributes(session):
    pass
    #fare_id,price,currency_type,payment_method,transfers,transfer_duration

def load_bus_fare_rules(session):
    pass
    #fare_id,origin_id,destination_id

#############################

def load_rails_routes(session):
    pass
    #route_id,route_short_name,route_long_name,route_desc,agency_id,route_type,route_color,route_text_color,route_url

def load_rails_stops(session):
    pass
    #stop_id,stop_name, stop_desc, stop_lat, stop_lon, zone_id

def load_rails_stop_times(session):
    pass
    #trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type

def load_rails_trips(session):
    pass
    #route_id,service_id,trip_id,trip_headsign,block_id,trip_short_name,shape_id,direction_id

def load_rails_transfers(session):
    pass
    #from_stop_id,to_stop_id,transfer_type

def load_rails_agency(session):
    pass
    #agency_id, agency_name, agency_url, agency_timezone, agency_lang


