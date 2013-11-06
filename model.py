import config
# import bcrypt
# from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text, Float

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

#from flask.ext.login import UserMixin

engine = create_engine(config.DB_URI, echo=True) 
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

################################################

# class User(Base, UserMixin):
#     __tablename__ = "users" 
#     id = Column(Integer, primary_key=True)
#     f_name = Column(String(64), nullable=False)
#     l_name = Column(String(64), nullable=False)
#     email = Column(String(64), nullable=False)
#     password = Column(String(64), nullable=False)
#     salt = Column(String(64), nullable=False)

#     posts = relationship("Post", uselist=True)

#     def set_password(self, password):
#         self.salt = bcrypt.gensalt()
#         password = password.encode("utf-8")
#         self.password = bcrypt.hashpw(password, self.salt)

#     def authenticate(self, password):
#         password = password.encode("utf-8")
#         return bcrypt.hashpw(password, self.salt.encode("utf-8")) == self.password

# class Post(Base):
#     __tablename__ = "posts"
    
#     id = Column(Integer, primary_key=True)
#     title = Column(String(64), nullable=False)
#     body = Column(Text, nullable=False)
#     created_at = Column(DateTime, nullable=False, default=datetime.now)
#     posted_at = Column(DateTime, nullable=True, default=None)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User")

##############################################

class BusRoutes(Base):
    __tablename__ = "bus_routes"

    route_id = Column(Integer, primary_key=True)
    route_short_name = Column(Integer, nullable=False)
    route_long_name = Column(String(64), nullable=False)
    route_type = Column(Integer, nullable=False)
    route_color = Column(String(64), nullable=True)
    route_text_color = Column(String(64), nullable=True)
    route_url = Column(String(128), nullable=True)


class BusStops(Base):
    __tablename__ = "bus_stops"
    stop_id = Column(Integer, primary_key=True)
    stop_name = Column(String(64), nullable=False)
    stop_lat = Column(Float, nullable=False)
    stop_lon = Column(Float, nullable=False)
    location_type = Column(String(64), nullable=True)
    parent_station = Column(Integer, nullable=True)
    zone_id = Column(Integer, nullable=True)
    wheelchair_boarding = Column(Integer, nullable=True)




class BusStopTimes(Base):
    __tablename__ = "bus_stop_times"
    trip_id = Column(Integer, primary_key=True)
    arrival_time = Column(Integer, nullable=False)
    departure_time = Column(Integer, nullable=False)
    stop_id = Column(Integer, nullable=False)
    stop_sequence = Column(Integer, nullable=False)




class BusTrips(Base):
    __tablename__ = "bus_trips"
    route_id = Column(Integer, primary_key=True)
    service_id = Column(Integer, nullable=False)
    trip_id = Column(Integer, nullable=False)
    trip_headsign = Column(String(64), nullable=False)
    block_id = Column(Integer, nullable=False)
    direction_id = Column(Integer, nullable=False)
    shape_id = Column(Integer, nullable=False)




class BusTransfers(Base):
    __tablename__ = "bus_transfers"
    id = Column(Integer, primary_key=True)
    from_stop_id = Column(Integer, nullable=False)
    to_stop_id = Column(Integer, nullable=False)
    transfer_type = Column(Integer, nullable=True)
    min_transfer_time = Column(String(64), nullable=True)




class BusAgency(Base):
    __tablename__ = "bus_agency"
    agency_id = Column(Integer, primary_key=True)
    agency_name = Column(String(64), nullable=False)
    agency_url = Column(String(64), nullable=False)
    angency_timezone = Column(String(64), nullable=False)
    agency_lang = Column(String(64), nullable=False)
    agency_fare_url = Column(String(64), nullable=False)




class BusFareAttributes(Base):
    __tablename__ = "bus_fare_attributes"
    fare_id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    currency_type = Column(String(64), nullable=False)
    payment_method = Column(Integer, nullable=False)
    transfers = Column(Integer, nullable=False)
    transfer_duration = Column(Integer, nullable=False)



class BusFareRules(Base):
    __tablename__ = "bus_fare_rules"
    id = Column(Integer, primary_key=True)
    fare_id = Column(Integer, nullable=False)
    origin_id = Column(Integer, nullable=False)
    destination_id = Column(Integer, nullable=False)

# ##########################################



class RailsRoutes(Base):
    __tablename__ = "rails_routes"
    id = Column(Integer, primary_key=True)
    route_id = Column(String(64), nullable=False)
    route_short_name = Column(String(64), nullable=False)
    route_long_name = Column(String(64), nullable=False)
    route_desc = Column(String(64), nullable=True)
    agency_id = Column(String(64), nullable=False)
    route_type = Column(Integer, nullable=False)
    route_color = Column(String(64), nullable=False)
    route_text_color = Column(String(64), nullable=False)
    route_url = Column(String(64), nullable=False)



class RailsStops(Base):
    __tablename__ = "rails_stops"
    stop_id = Column(Integer, primary_key=True)
    stop_name = Column(String(64), nullable=False)
    stop_desc = Column(String(64), nullable=False)
    stop_lat = Column(Float, nullable=False)
    stop_lon = Column(Float, nullable=False)
    zone_id = Column(Integer, nullable=False)


class RailsStopTimes(Base):
    __tablename__ = "rails_stop_times"
    id = Column(Integer, primary_key=True)
    trip_id = Column(String(64), nullable=False)
    arrival_time = Column(Integer, nullable=False)
    departure_time = Column(Integer, nullable=False)
    stop_id = Column(Integer, nullable=False)
    stop_sequence = Column(Integer, nullable=False)
    pickup_type = Column(Integer, nullable=False)
    drop_off_type = Column(Integer, nullable=False)



class RailsTrips(Base):
    __tablename__ = "rails_trips"
    id = Column(Integer, primary_key=True)
    route_id = Column(String(64), nullable=False)
    service_id = Column(String(64), nullable=False)
    trip_id = Column(String(64), nullable=False)
    trip_headsign = Column(String(64), nullable=False)
    block_id = Column(Integer, nullable=False)
    trip_short_name = Column(Integer, nullable=False)
    shape_id = Column(String(64), nullable=False)
    direction_id = Column(Integer, nullable=False)



class RailsTransfers(Base):
    __tablename__ = "rails_transfers"
    id = Column(Integer, primary_key=True)
    from_stop_id = Column(Integer, nullable=False)
    to_stop_id = Column(Integer, nullable=False)
    transfer_type = Column(Integer, nullable=False)



class RailsAgency(Base):
    __tablename__ = "rails_agency"
    id = Column(Integer, primary_key=True)
    agency_id = Column(String(64), nullable=False)
    agency_name = Column(String(64), nullable=False)
    agency_url = Column(String(64), nullable=False)
    agency_timezone = Column(String(64), nullable=False)
    agency_lang = Column(String(64), nullable=False)

#########################################

def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    # create_tables()
    pass
