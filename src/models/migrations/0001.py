from peewee import *

def create_tables():

    from main import get_database
    from models.tag import Tag
    database = get_database()


    with database:
        database.create_tables([Tag])


if '__main__' == __name__:

    import sys
    from os.path import abspath, dirname, join
    BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
    sys.path.append(BASE_DIR)    
    create_tables()
