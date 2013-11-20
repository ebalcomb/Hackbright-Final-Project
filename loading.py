##finding the IDs of the accessible rails stops from the file "intrapaths", which I compiled myself with the SEPTA map.

def find_accessible_rails_stops():
    f = open("intrapaths.csv")
    stops = f.readlines()
    paths_stops = []
    for stop in stops:
        stop_col = stop.split(",")
        start_id = stop_col[0].strip()
        end_id = stop_col[1].strip()
        if int(start_id) not in paths_stops:
            paths_stops.append(int(start_id))
        if int(end_id) not in paths_stops:
            paths_stops.append(int(end_id))
    g = open("railschedules/stops.txt")
    rails = g.readlines()
    accessible_rails_stops = []
    for rail in rails:
        rail_col = rail.split(",")
        rail_id = rail_col[0].strip()
        if int(rail_id) in paths_stops:
            accessible_rails_stops.append(int(rail_id))
    for item in accessible_rails_stops:
        print item