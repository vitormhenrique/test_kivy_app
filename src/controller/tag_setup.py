
from functools import partial
from typing import List

from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineListItem
from models.tag import Tag
from views.screens import TagDetailScreen, TagSetupScreen

from controller.screen_controller import ScreenController


class TagSetupScreenController(ScreenController):

    def __init__(self) -> None:

        super().__init__()

        self.dialog = None
        self.view = TagSetupScreen(controller=self)

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def on_pre_enter(self):

        tags = Tag.select().order_by(Tag.order)

        for tag in tags:

            _func = partial(self.show_tag_detail_dialog, tag.id)

            list_item = TwoLineListItem(
                text=tag.name,
                secondary_text=f"Enabled: {tag.enabled} | Main {tag.is_main_tag} | Order {tag.order}",
                on_release=_func
            )

            self.view.ids.container.add_widget(list_item)

    def _update_list(self):

        tags = Tag.select()

        for tag in tags:
            for list_item in self.view.ids.container.children:
                if list_item.text == tag.name:
                    list_item.secondary_text = f"Enabled: {tag.enabled} | Main {tag.is_main_tag} | Order {tag.order}"

    def goto_parrent(self):

        self.view.screen_manager.switch_to(
            self.parent_view,
            direction='right',
            transition=SlideTransition()
        )

    def close_tag_detail_dialog(self, dialog):
        if self.dialog is not None:
            self.dialog.dismiss()
            self.dialog = None

    def edit_tag_detail(self, tag_id, dialog):
        tag: Tag = Tag.get(Tag.id == tag_id)

        tag.order = int(self.dialog.content_cls.ids.order.text)
        tag.enabled = self.dialog.content_cls.ids.is_enabled.ids.checkbox.active
        tag.is_main_tag = self.dialog.content_cls.ids.is_main.ids.checkbox.active

        tag.save()

        self._update_list()

        self.close_tag_detail_dialog(dialog)

    def show_tag_detail_dialog(self, tag_id, list_item):

        tag: Tag = Tag.get(Tag.id == tag_id)

        content = TagDetailScreen()

        content.ids.order.text = str(tag.order)
        content.ids.is_enabled.active = tag.enabled
        content.ids.is_main.active = tag.is_main_tag

        _func_close = partial(self.close_tag_detail_dialog)
        _func_edit = partial(self.edit_tag_detail, tag.id)

        if not self.dialog:
            self.dialog = MDDialog(
                title=tag.name,
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
