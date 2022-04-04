from peewee import *
from models.connection import BaseModel

class Migration(BaseModel):
    name = CharField()
    run_date = DateTimeField()
    
