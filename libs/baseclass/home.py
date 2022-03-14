from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

Builder.load_file("libs/kv/home.kv")


class ContentNavigationDrawer(MDBoxLayout):
    pass

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


