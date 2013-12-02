#!/bin/sh

# cut
# split
# grep
# uniq
# sort

for trip_id in `cat included_bus_trips`
do
grep -e "^$trip_id" stop_times.txt >> interesting_times.txt
done
