from peewee import *
from models.connection import BaseModel


# class Manufacturer(BaseModel):
#     name = CharField()

# class Model(BaseModel):
#     manufacturer = ForeignKeyField(Manufacturer, backref='models')
#     name = CharField()

# class Firmware(BaseModel):
#     model = ManyToManyField(Model, backref='firmware')
#     name = CharField()

class Asset(BaseModel):
    model = CharField()
    manufacturer = CharField()
    firmware = CharField()
    client = CharField()
    synced_with_sr = BooleanField(default=False)