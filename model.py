from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref



engine = create_engine("sqlite:///septa.db", echo=True)
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()



############################################################
#CLASSES

class Paths(Base):
    __tablename__ = "paths"
    id = Column(Integer, primary_key=True)
    start_stop = Column(Integer, ForeignKey('stops.id'), nullable=False)
    end_stop = Column(Integer, ForeignKey('stops.id'), nullable=False)
    cost = Column(Integer, nullable=False)


class Routes(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True)
    route_short_name = Column(Integer, nullable=False)
    route_long_name = Column(String(64), nullable=False)
    route_type = Column(String(64), nullable=False)


class Stops(Base):
    __tablename__ = "stops"
    id = Column(Integer, primary_key=True)
    stop_name = Column(String(64), nullable=False)
    stop_lat = Column(Float, nullable=True)
    stop_lon = Column(Float, nullable=True)
    stop_type = Column(String(64), nullable=False)
    
    # stop_times = relationship("StopTimes", backref=backref("stop", order_by=id))
    # trips = relationship("Trips", backref=backref("stops", order_by=id))
    # paths = relationship("Paths", backref=backref("stops", order_by=id))

class StopTimes(Base):
    __tablename__ = "stop_times"
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    arrival_time = Column(String(64), nullable=False)
    stop_id = Column(Integer, ForeignKey('stops.id'), nullable=False)

    # stop = relationship("Stops", backref=backref("stop_times", order_by=id))


class Trips(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    direction_id = Column(Integer, nullable=False)



class ShortestRoute(Base):
    __tablename__ = "shortest_routes"
    id = Column(Integer, primary_key=True)
    start_stop = Column(Integer, ForeignKey('stops.id'), nullable=False)
    end_stop = Column(Integer, ForeignKey('stops.id'), nullable=False)
    stops_hit = Column(String(200), nullable=False)




############################################################
#FUNCTIONS
#check the accessbility of stops found within the radius around the starting lat/long. If a stop is accessible, return that stops details. If it gets through the whole list and no stops are accessible, return False. 


def access_check(stop_list):
    for stop in stop_list:
        stop = int(stop)
        stop_access = session.query(Stops).filter_by(id=stop).all()
        if stop_access:
            print "WINNER: ", stop
            return stop
    return False


def get_paths():
    paths = session.query(Paths).all()
    return paths


def get_stops():
    stops = session.query(Stops).all()
    return stops


def get_stop(stop_id):
    stop = session.query(Stops).filter_by(id=int(stop_id)).all()
    return stop[0]


def get_shortest_route(start_stop, end_stop):
    shortest_route = session.query(ShortestRoute).filter_by(start_stop=start_stop, end_stop=end_stop).all()
    stop_names = []
    if shortest_route:
        route_string = shortest_route[0].stops_hit
        route_string = route_string.split(",")
        for stop in route_string:
            stop_object = session.query(Stops).filter_by(id=int(stop)).all()
            stop_name = stop_object[0].stop_name
            stop_names.append(stop_name)
        return ", ".join(stop_names)

    else:
        return False
        




##########################################
#CREATE


def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
