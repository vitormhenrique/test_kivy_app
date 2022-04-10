from peewee import *

def do_something():


    from models.settings import Keys

    sr_url = "http://10.0.0.229:8000/"

    if sr_url[-1] == '/':
        sr_url = sr_url[:-1]


if '__main__' == __name__:

    import sys
    from os.path import abspath, dirname, join
    BASE_DIR = dirname(dirname(abspath(__file__)))
    sys.path.append(BASE_DIR)    
    # BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
    # sys.path.append(BASE_DIR)   
    do_something()
