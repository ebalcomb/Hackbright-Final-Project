

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


    stops = []
    for row in rows:
        if row[0] not in stops:
            stops.append(row[0])
        if (row[1]) not in stops:
            stops.append(row[1])
    print "stops: ", stops

    paths = {}
    for stop in stops:
        paths[stop] = []
    for row in rows:
        paths[row[0]].extend([row[1]])
        #paths[row[1]].extend([row[0]])
    print "paths", paths

    distances = {}
    for row in rows:
        distances[row[0], row[1]] = row[2]
    print "distances", distances

    # my_map = Map(paths=paths, stops=stops, distances=distances)
    # return my_map