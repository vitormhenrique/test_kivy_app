from peewee import *
from models.connection import BaseModel

class Tag(BaseModel):
    name = CharField()
    enabled = BooleanField()
    is_main_tag = BooleanField()
    order = IntegerField()
    
class TagValue(BaseModel):
    from models.asset import Asset
    tag = ForeignKeyField(Tag, backref='tags')
    asset = ForeignKeyField(Asset, backref='tags')
    value = CharField()