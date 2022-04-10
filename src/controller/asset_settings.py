
from functools import partial

from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineListItem
from models.settings import Keys, Settings
from views.screens import AssetSettingsScreen, DefaultSettingValue

from controller.screen_controller import ScreenController
from controller.tag_setup import TagSetupScreenController


class AssetSettingsScreenController(ScreenController):

    def __init__(self, model) -> None:

        super().__init__()

        self.screens = {
            "Tag Setup": {
                "controller": TagSetupScreenController,
            },
        }

        self.view = AssetSettingsScreen(controller=self)
        self.dialog = None

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def transition_to_screen(self, screen_name):

        controller = self.screens[screen_name]["controller"]()
        view = controller.get_screen()
        view.screen_manager = self.view.screen_manager
        view.name = screen_name
        controller.parent_view = self.view

        self.view.screen_manager.switch_to(
            view, direction='left', transition=SlideTransition())

    def on_pre_enter(self):
        self.update_setting_ui()

    def close_dialog(self, dialog):
        if self.dialog is not None:
            self.dialog.dismiss()
            self.dialog = None

    def edit_setting(self, setting_key, btn):

        setting = Settings.get(Settings.key == setting_key.key_value)

        setting.value = self.dialog.content_cls.ids.setting_value.text

        setting.save()

        self.update_setting_ui()

        self.close_dialog(btn)

    def update_setting_ui(self):

        self.view.ids.setting_container.clear_widgets()

        for key in Keys:

            _value = ""

            try:
                _value = Settings.get(Settings.key == key.key_value).value
            except Settings.DoesNotExist:
                pass

            _func = partial(self.show_edit_dialog, key, _value)

            list_item = TwoLineListItem(
                text=key.key_text,
                secondary_text=f"Current value: {_value}",
                on_release=_func
            )

            self.view.ids.setting_container.add_widget(list_item)

    def show_edit_dialog(self, setting_key, current_value, line):
        _func_close = partial(self.close_dialog)
        _func_edit = partial(self.edit_setting, setting_key)

        content = DefaultSettingValue()

        content.ids.setting_value.text = str(current_value)

        if not self.dialog:
            self.dialog = MDDialog(
                title="Edit Setting",
                type="custom",
                content_cls=content,
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        on_release=_func_close,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=_func_edit,
                    ),
                ],
            )
        self.dialog.open()
