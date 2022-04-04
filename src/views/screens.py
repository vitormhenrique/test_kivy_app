
from views.base_screen import BaseScreenView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty


class LabelScannerScreen(BaseScreenView):
    current_scan_id = ObjectProperty()

class TagDetailScreen(MDBoxLayout):
    pass

class TagSetupScreen(BaseScreenView):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass

class RootScreen(BaseScreenView):
    pass

class HomeScreen(BaseScreenView):

    def on_enter(self):
        self.ids.toolbar.title = "Home"

class AssetSettingsScreen(BaseScreenView):
   
    def on_enter(self):
        self.ids.toolbar.title = "Asset Settings"