
from views.screens import HomeScreen

class HomeScreenController:

    def __init__(self, model) -> None:
        
        self.view = HomeScreen(controller=self)

    def get_screen(self):
        """The method creates get the view."""

        return self.view