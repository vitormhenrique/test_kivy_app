from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.widget import MDWidget
from kivy.clock import Clock

from kivymd.uix.textfield import MDTextField
from kivymd.uix.relativelayout import MDRelativeLayout


class ScanInput(MDTextField):
    # def on_focus(self, *args):
    #     if kivy.utils.platform == 'android':
    #         self._unbind_keyboard()
    pass


# class ScanInput(MDTextField):
#     def _on_focus(self, *args):
#         super()._on_focus(*args)
#         self.hide_keyboard()
class TagScan(MDBoxLayout):
    tag_id = ObjectProperty()
    text = ObjectProperty()
    # order = ObjectProperty()

class SpinnerContent(MDRelativeLayout):
    pass

class MainToolbar(MDToolbar):
    pass




class OneLineListItemAligned(OneLineListItem):
    def __init__(self,halign,  **kwargs):
        super(OneLineListItemAligned, self).__init__(**kwargs)
        # if halign is not None:
        self.ids._lbl_primary.halign = halign

class OneLineListItemAlignedCenter(OneLineListItem):
    def __init__(self, **kwargs):
        super(OneLineListItem, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui, 0)

    def init_ui(self, dt=0):
        self.ids._lbl_primary.halign = 'center'


class PaginationOneLineListItemAligned(OneLineListItemAligned):

    def __init__(self,**kwargs):
        super(PaginationOneLineListItemAligned, self).__init__(**kwargs)

    def set_page(self, current, number_of_pages):
        self.text = f"Asset {current} of {number_of_pages}"