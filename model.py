import config
import bcrypt
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text, Float

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

#from flask.ext.login import UserMixin


engine = create_engine("sqlite:///septa.db", echo=True)
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()


###############################################


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
    #stop_times = relationship("StopTimes", backref=backref("stop", order_by=id))
    #trips = relationship("Trips", backref=backref("stops", order_by=id))
    #paths = relationship("Paths", backref=backfref("stops", order_by=id))

class StopTimes(Base):
    __tablename__ = "stop_times"
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    arrival_time = Column(Integer, nullable=False)
    stop_id = Column(Integer, ForeignKey('stops.id'), nullable=False)

    #stop = relationship("Stops", backref=backref("stop_times", order_by=id))


class Trips(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    direction_id = Column(Integer, nullable=False)




##########################################

def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    # create_tables()
    pass
