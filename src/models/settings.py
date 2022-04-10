from unittest.mock import DEFAULT
from peewee import *
from models.connection import BaseModel
from utility.enum_extender import SettingChoicesEnum

class Keys(SettingChoicesEnum):
    DEFAULT_MODEL = "default_model", "Default Model", True
    DEFAULT_FIRMWARE = "default_firmware", "Default Firmware", True
    DEFAULT_MANUFACTURER = "default_manufacturer", "Default Manufacturer", True
    DEFAULT_CLIENT = "default_client", "Default Client", True
    DEFAULT_LOCATION = "default_location", "Default Location", True

class Settings(BaseModel):
    key = CharField()
    value = CharField()
    visible = BooleanField(default=True)