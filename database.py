import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Activity(db.Model):
    '''
    Database Model to Log the Activity of the Sensor for creating Charts along the way
    '''
    id: Mapped[Integer] = mapped_column(primary_key=True)
    sensor: Mapped[String] = mapped_column(ForeignKey("Sensors.id"),)
    temperature: Mapped[Integer] = mapped_column(Integer)
    humidity: Mapped[Integer] = mapped_column(Integer)
    time: Mapped[datetime.datetime] = mapped_column(
       DateTime(timezone=True), server_default=func.now()
    )

class Sensors(db.Model):
   '''
   Database Model to Map the TP357-Name/Id to a Local Location

   E.g. - E3717 has location Bathroom 
   '''
   id: Mapped[String] = mapped_column(primary_key=True)
   location: Mapped[String] = mapped_column(String)
