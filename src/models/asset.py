from peewee import *
from models.connection import BaseModel


class Manufacturer(BaseModel):
    name = CharField()

class Model(BaseModel):
    manufacturer = ForeignKeyField(Manufacturer, backref='models')
    name = CharField()

class Firmware(BaseModel):
    model = ManyToManyField(Model, backref='firmware')
    name = CharField()

class Asset(BaseModel):
    model = ForeignKeyField(Model, backref='assets')
    firmware = ForeignKeyField(Firmware, backref='assets')
    owner = CharField()
    synced_with_sr = BooleanField(default=False)


# class MinerManufacturers(models.TextChoices):
#     CANAAN = 'Canaan', 'Canaan'
#     BITMAIN = 'Bitmain', 'Bitmain'
#     MICROBT = 'Microbt', 'Microbt'
# class MinerFirmware(models.TextChoices):
#     CGMINER = 'Cgminer', 'Cgminer'
#     BMMINER = 'Bmminer', 'Bmminer'
#     ASICSEER = 'Asicseer', 'Asicseer'
#     BTMINER = 'Btminer', 'Btminer'
#     ENIGMA = 'Enigma', 'Enigma'
#     VNISH = 'Vnish', 'Vnish'
# class MinerModels(models.TextChoices):
#     AVALON_A851 = 'A851', 'Avalon A851'
#     AVALON_A10 = 'A10', 'Avalon A10'
#     ANTMINER_S9 = 'S9', 'Antminer S9'
#     ANTMINER_S19 = 'S19', 'Antminer S19'
#     WHATSMINER_M30S = 'M30S', 'Whatsminer M30S'
#     WHATSMINER_M30SI = 'M30SI', 'Whatsminer M30Si'
#     WHATSMINER_M31S = 'M31S', 'Whatsminer M31S'
#     WHATSMINER_M31SI = 'M31SI', 'Whatsminer M31Si'