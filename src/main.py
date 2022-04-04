'''
'''
import os
import sys
from pathlib import Path

import pandas as pd
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from peewee import SqliteDatabase

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["SR_MOBILE_ROOT"] = sys._MEIPASS
else:
    os.environ["SR_MOBILE_ROOT"] = str(Path(__file__).parent)

DATABASE_FILE = f"{os.environ['SR_MOBILE_ROOT']}/sr_mobile.db"


def get_database():
    return SqliteDatabase(DATABASE_FILE)


KV = '''
Label:
    text: app.result
    text_size: self.width, None
    halign: 'center'
'''
data = [['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3']]

df = pd.DataFrame(data)

class Application(App):
    result = StringProperty('')
    def build(self):
        self.database = get_database()
        self.result = format(df)
        return Builder.load_string(KV)


if __name__ == "__main__":
    Application().run()
