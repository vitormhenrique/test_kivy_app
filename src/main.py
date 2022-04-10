import os
import sys
from pathlib import Path

from kivy.clock import mainthread
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from peewee import SqliteDatabase

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["APP_MOBILE_ROOT"] = sys._MEIPASS
else:
    os.environ["APP_MOBILE_ROOT"] = str(Path(__file__).parent)

DATABASE_FILE = f"{os.environ['APP_MOBILE_ROOT']}/app.db"


Window.softinput_mode = 'below_target'

def get_database():
    return SqliteDatabase(DATABASE_FILE)

class SRMobile(MDApp):
    def __init__(self, **kwargs):
        from controller.root import RootScreenController
        super().__init__(**kwargs)
        self.KV_DIR = os.path.join(os.environ['APP_MOBILE_ROOT'], "views")
        self.load_all_kv_files()
        self.title = "SR Mobile"
        self.database = get_database()
        self.controller = RootScreenController()
        self.loading_dialog = None

    def load_all_kv_files(self):
        for dir, dirs, files in os.walk(self.KV_DIR):
            for file in files:
                if file.endswith(".kv"):
                    path = os.path.join(dir, file)
                    with open(path, encoding="utf-8") as kv:
                        Builder.load_string(kv.read())

    def build(self):
        return self.controller.get_screen()

    @mainthread
    def start_loading_screen(self, *args):

        if self.loading_dialog is None:
            from views.components import SpinnerContent

            self.loading_dialog = MDDialog(
                title="Loading...",
                content_cls=SpinnerContent(),
                type="custom",
                auto_dismiss=False,
            )
            self.loading_dialog.open()

    def close_loading_screen(self, *args):

        if self.loading_dialog is not None:
            self.loading_dialog.dismiss()
            self.loading_dialog = None


if '__main__' == __name__:
    SRMobile().run()
