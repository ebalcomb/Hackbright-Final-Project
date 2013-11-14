

def get_trip_per_route():
	f = open("busschedules/trips.txt")
	r = f.readlines()

	used_routes = []
	trips = []

	for row in r:
		row = row.strip()
		row = row.split(",")
		if int(row[0]) not in used_routes:
			used_routes.append(int(row[0]))
			trips.append(int(row[2]))
	return trips

def get_stops_per_trip():
	trips = get_trip_per_route()

	f = open("busschedules/stop_times.txt")
	r = f.readlines()

	rows = []
	tuples = []


	for row in r:
		row = row.strip()
		row = row.split(",")
		if int(row[0]) in trips:
			rows.append(row)


	for i in range(len(rows)-2):
		if rows[i][0] == rows[i+1][0]:
			tuples.append((int(rows[i][3]), int(rows[i+1][3]), 5, 0))
	
	for item in tuples:
		print item


def format_file():
	f = open("internames2.csv")
	r = f.readlines()

	fixed_lines = []
	for row in r:
		row = row.strip()
		row = row.split(",")
		fixed_lines.append((2, row[0], row[1]))

	for item in fixed_lines:
		print item[0], ",", item[1], ",", item[2]






