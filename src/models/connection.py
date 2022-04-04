from peewee import *

class BaseModel(Model):
    """A base model that will use our database"""

    class Meta:
        from main import get_database
        database = get_database()