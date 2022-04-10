
from views.base_screen import BaseScreenView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from kivy.logger import Logger

class LabelScannerScreen(BaseScreenView):
    current_scan_id = ObjectProperty()

class DefaultSettingValue(MDBoxLayout):
    """
    POP UP content for the setting
    Args:
        MDBoxLayout (_type_): _description_
    """
    pass
class TagDetailScreen(MDBoxLayout):
    """
    POP UP content for the setting the tag detail
    Args:
        MDBoxLayout (_type_): _description_
    """
    pass

class TagSetupScreen(BaseScreenView):
    pass

# class ContentNavigationDrawer(MDBoxLayout):
#     pass

class RootScreen(BaseScreenView):
    def on_enter(self):
        Logger.info("on enter root")

    def on_leave(self):
        Logger.info("on leave root")

class HomeScreen(BaseScreenView):

    def on_enter(self):
        self.ids.toolbar.title = "Home"

class AssetSettingsScreen(BaseScreenView):
   
    def on_enter(self):
        self.ids.toolbar.title = "Asset Settings"

class AssetTableScreen(BaseScreenView):
    def on_enter(self):
        self.ids.toolbar.title = "Scanned Assets"