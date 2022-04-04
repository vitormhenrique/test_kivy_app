
from views.screens import AssetSettingsScreen

from controller.tag_setup import TagSetupScreenController
from kivy.uix.screenmanager import SlideTransition

class AssetSettingsScreenController:

    def __init__(self, model) -> None:

        self.screens = {
        "Tag Setup": {
            "controller": TagSetupScreenController,
        },
    }
        
        self.view = AssetSettingsScreen(controller=self)

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def transition_to_screen(self, screen_name):
        
        controller = self.screens[screen_name]["controller"]()
        view = controller.get_screen()
        view.screen_manager = self.view.screen_manager
        view.name = screen_name
        controller.parent_view = self.view

        self.view.screen_manager.switch_to(view, direction='left', transition=SlideTransition())
