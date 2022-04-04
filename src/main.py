import os
import sys
from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp

from peewee import SqliteDatabase

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["SR_MOBILE_ROOT"] = sys._MEIPASS
else:
    os.environ["SR_MOBILE_ROOT"] = str(Path(__file__).parent)

DATABASE_FILE = f"{os.environ['SR_MOBILE_ROOT']}/sr_mobile.db"


def get_database():
    return SqliteDatabase(DATABASE_FILE)
    # None

class SRMobile(MDApp):
    def __init__(self, **kwargs):
        from controller.root import RootScreenController
        super().__init__(**kwargs)
        self.KV_DIR = os.path.join(os.environ['SR_MOBILE_ROOT'], "views")
        self.load_all_kv_files()
        self.title = "SR Mobile"
        self.database = get_database()
        self.controller = RootScreenController()

    def load_all_kv_files(self):
        for dir, dirs, files in os.walk(self.KV_DIR):
            for file in files:
                if file.endswith(".kv"):
                    path = os.path.join(dir, file)
                    with open(path, encoding="utf-8") as kv:
                        Builder.load_string(kv.read())



    def build(self):
        return self.controller.get_screen()

    def on_start(self):
        self.root.dispatch("on_enter")


if '__main__' == __name__:
    SRMobile().run()