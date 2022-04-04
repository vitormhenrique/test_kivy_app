from peewee import *
from pathlib import Path
from datetime import datetime


def migrate():

    from main import get_database
    from models.tag import TagValue
    from models.migration import Migration
    from models.settings import Settings
    from models.asset import Manufacturer, Model, Firmware, Asset

    database = get_database()


    with database:
        database.create_tables([Migration, Settings, Manufacturer, Model, Firmware, Asset])
        database.create_tables([TagValue])


        migration_name = Path(__file__).stem
        migration = Migration(name=migration_name, run_date=datetime.now())
        migration.save()


if '__main__' == __name__:

    import sys
    from os.path import abspath, dirname, join
    BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
    sys.path.append(BASE_DIR)    
    migrate()
