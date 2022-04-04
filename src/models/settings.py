from unittest.mock import DEFAULT
from peewee import *
from models.connection import BaseModel
from utility.enum_extender import ChoicesEnum

class Keys(ChoicesEnum):
    DEFAULT_MODEL = "default_model", "Default Model"
    DEFAULT_FIRMWARE = "default_firmware", "Default Firmware"
    DEFAULT_MANUFACTURER = "default_manufacturer", "Default Manufacturer"
    DEFAULT_OWNER = "default_owner", "Default Owner"

class Settings(BaseModel):
    key = CharField()
    value = CharField()