from kivy.properties import ObjectProperty
from views.screens import RootScreen

from controller.asset_settings import AssetSettingsScreenController
from controller.asset_table import AssetTableScreenController
from controller.home import HomeScreenController
from controller.label_scanner import LabelScannerScreenController

from controller.screen_controller import ScreenController


class RootScreenController(ScreenController):

    screens = {
        "Home": {
            "model": None,
            "controller": HomeScreenController,
        },
        "Asset Setup": {
            "model": None,
            "controller": AssetSettingsScreenController,
        },
        "Scan Labels": {
            "model": None,
            "controller": LabelScannerScreenController,
        },
        "Assets": {
            "model": None,
            "controller": AssetTableScreenController,
        },
    }

    def __init__(self) -> None:

        super().__init__()

        self.view = RootScreen(controller=self, name="root")

        # self.screen_manager = self.view.ids.screen_manager

        for i, name_screen in enumerate(self.screens.keys()):
            model = self.screens[name_screen]["model"]
            controller = self.screens[name_screen]["controller"](model)
            view = controller.get_screen()
            # view.screen_manager = self.screen_manager
            view.name = name_screen
            self.view.ids.screen_manager.add_widget(view)

        # self.view.ids.screen_manager.add_widget(view)

    def get_screen(self):
        """The method creates get the view."""

        # return self.view.ids.screen_manager
        return self.view

    def transition_to_screen(self, screen_name):

        self.view.ids.screen_manager.current = screen_name

