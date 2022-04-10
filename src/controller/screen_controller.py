from models.asset import Asset
from abc import ABC
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.logger import Logger


class ScreenController(ABC):

    app: MDApp = None
    window = None

    def __init__(self) -> None:
        super().__init__()

        self.app = MDApp.get_running_app()
        self.window = Window

    def snack_message(self, text, color="575757", duration=2):
        Snackbar(
            text=text,
            duration=duration,
            bg_color=get_color_from_hex(color),
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(self.window.width - (dp(10) * 2)) / self.window.width
        ).open()


    def success_snack(self, text="Success"):
        self.snack_message(text, color="018786", duration=1)

    def error_snack(self, text):
        self.snack_message(text, color="B00020", duration=3)
