
from faulthandler import disable
from functools import partial

from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from models.asset import Asset
from models.settings import Keys, Settings
from models.tag import Tag, TagValue
from views.components import (OneLineListItemAligned,
                              PaginationOneLineListItemAligned, TagScan)
from views.screens import LabelScannerScreen


class LabelScannerScreenController:

    def __init__(self, model) -> None:

        self.screens = {
            "Tag Setup": {
                "controller": LabelScannerScreen,
            },
        }

        self.view = LabelScannerScreen(controller=self)
        self._widgets_added = False
        self._tags = None
        self._current_tag_focus = 0
        self.ui_tags = None

        self._asset_model = ""
        self._asset_firmware = ""
        self._asset_owner = ""

        self._assets = None

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def on_pre_enter(self):

        if self.ui_tags is not None:
            self.clear_scan()

    def __load_settings(self):
        _asset_firmware = Settings.get(Settings.key==Keys.DEFAULT_FIRMWARE.key_value)
        if _asset_firmware:
            self._asset_firmware = _asset_firmware.value

        _asset_model = Settings.get(Settings.key==Keys.DEFAULT_MODEL.key_value)
        if _asset_model:
            self._asset_model = _asset_model.value

        _asset_owner = Settings.get(Settings.key==Keys.DEFAULT_OWNER.key_value)
        if _asset_owner:
            self._asset_owner = _asset_owner.value


    def on_enter(self):
        self._current_tag_focus = 0

        self.view.ids.header_content.clear_widgets()

        self.page_detail = PaginationOneLineListItemAligned(
            halign="right", disabled=True, divider=None)

        self.__load_settings()

        self._assets = Asset.select()

        self._tags = Tag.select().order_by(Tag.order)
        self._total_assets = self._assets.count() + 1
        self._current_asset = self._assets.count() + 1

        self.__load_tag_ui_input()


    def __load_tag_ui_input(self):
        self.page_detail.set_page(current=self._current_asset, number_of_pages=self._total_assets)

        self.model_detail = OneLineListItemAligned(halign="center", text=self._asset_model, divider="Full", disabled=True)

        self.view.ids.header_content.add_widget(self.page_detail)
        self.view.ids.header_content.add_widget(self.model_detail)

        self.view.ids.tag_scan_content.clear_widgets()

        self.ui_tags = []

        for tag in self._tags:
            ui_tag = TagScan(text=tag.name, tag_id=tag.id)

            _func = partial(self.handle_text_input, ui_tag)

            ui_tag.ids.input_code.on_text_validate = _func

            self.ui_tags.append(ui_tag)

            self.view.ids.tag_scan_content.add_widget(
                ui_tag
            )

        Clock.schedule_once(self.set_ui_focus, 0)

    def _load_asset(self):
        
        if self._current_asset <= self._assets.count():
            
            _asset = self._assets[self._current_asset-1]

            # _tags_value = TagValue.select(TagValue.asset==_asset)
            _tags_value = TagValue.select().where(TagValue.asset==_asset)

            for tag_value in _tags_value:
                for ui_tag in self.ui_tags:
                    if tag_value.tag.id == ui_tag.tag_id:
                        ui_tag.ids.input_code.text = tag_value.value


    def set_ui_focus(self, *args):
        self.ui_tags[self._current_tag_focus].ids.input_code.focus = True


    def handle_text_input(self, instance: TagScan):
        self._current_tag_focus = self._current_tag_focus + 1

        if self._current_tag_focus < self._tags.count():
            self.set_ui_focus()
        else:
            self.save_and_next()


    def previous_scan(self, *args):
        self.clear_scan()
        self._current_asset = max(1, self._current_asset - 1)
        self.page_detail.set_page(current=self._current_asset, number_of_pages=self._total_assets)
        self._load_asset()

    def _valid_tags(self):

        for ui_tag in self.ui_tags:
            if ui_tag.ids.input_code.text is not None and ui_tag.ids.input_code.text != "":
                return True

        return False


        
    def save_and_next(self, *args):
        self._current_tag_focus = 0

        if not self._valid_tags():
            Snackbar(
                text="At least one tag is necessary",
                snackbar_animation_dir="Top"
            ).open()

        else:
            Snackbar(
                text="Saved with success",
                snackbar_animation_dir="Top"
            ).open()

            if self._current_asset <= self._assets.count():
                asset = self._assets[self._current_asset-1]
            else:
                asset = Asset(model=self._asset_model, firmware=self._asset_firmware, owner=self._asset_owner)

                asset.save()

            for ui_tag in self.ui_tags:

                _val = ui_tag.ids.input_code.text

                if _val is None or _val == "":
                    continue

                tag_val =  TagValue.select().where(TagValue.asset==asset, TagValue.tag == ui_tag.tag_id).first()

                if tag_val is None:
                    tag_val = TagValue(asset=asset,tag=ui_tag.tag_id, value=_val)
                else:
                    tag_val.value = _val
                
                tag_val.save()

            self._current_asset = self._current_asset + 1
            self.page_detail.set_page(current=self._current_asset, number_of_pages=self._total_assets)
            
        self.clear_scan()
        self._load_asset()
        self.set_ui_focus()

    def clear_scan(self, *args):
        for ui_tag in self.ui_tags:
            ui_tag.ids.input_code.text = ""
