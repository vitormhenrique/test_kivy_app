
from models.asset import Asset
from views.screens import HomeScreen
from controller.screen_controller import ScreenController

class HomeScreenController(ScreenController):

    def __init__(self, model) -> None:

        super().__init__()
        
        self.view = HomeScreen(controller=self)

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def on_pre_enter(self):

        total = Asset.select().count()
        synced = Asset.select().where(Asset.synced_with_sr==True).count()
        not_synced = Asset.select().where(Asset.synced_with_sr==False).count()
        
        self.view.ids.total_assets_scanned.secondary_text = str(total)
        self.view.ids.assets_scanned_not_synced.secondary_text = str(not_synced)
        self.view.ids.assets_scanned_synced.secondary_text = str(synced)
