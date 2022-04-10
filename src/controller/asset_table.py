import traceback
from time import time

import pandas as pd
import requests
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from models.asset import Asset
from models.settings import Keys, Settings
from models.tag import Tag, TagValue
from views.screens import AssetTableScreen

from controller.screen_controller import ScreenController


class AssetTableScreenController(ScreenController):

    def __init__(self, model) -> None:

        super().__init__()

        self.screens = {
            "Tag Setup": {
                "controller": AssetTableScreen,
            },
        }

        self.view = AssetTableScreen(controller=self)
        self._start_time = None


    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def _get_asset_data(self):

        tagval = TagValue.select(
            Asset.id,
            Asset.model,
            Asset.firmware,
            Asset.client,
            Asset.manufacturer,
            TagValue.value,
            Tag.name
        ).join_from(TagValue, Asset).join_from(TagValue, Tag).where(Asset.synced_with_sr==False)

        if tagval:

            df = pd.DataFrame(tagval.dicts())

            df = df.set_index(['id', 'model', 'firmware', 'client',
                            'name', 'manufacturer'], drop=True).unstack('name')

            df = df.droplevel(0, axis=1).reset_index()

            return df

        return pd.DataFrame()
    
    def on_pre_leave(self):
        Logger.debug("cleaning widgets")

    def on_pre_enter(self):
        Clock.schedule_once(self._load_screen, 0)

    def _load_screen(self, *args):
        # Clock.schedule_once(self.app.start_loading_screen(), 0)
        # self.app.start_loading_screen()

        self._start_time = time()

        df = self._get_asset_data()

        column_head = []
        row_values = []

        if not df.empty:
            for column in df.columns:
                _size = dp(max(int(len(column)*3.5), 20))
                column_head.append((column.title(), _size))

            row_values = df.values.tolist()

        use_pagination = False

        if len(row_values) > 10:
            use_pagination = True

        data_tables = MDDataTable(
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=use_pagination,
            check=False,
            rows_num=10,
            column_data=column_head,
            row_data=row_values,
        )
        data_tables.ids.container.add_widget(
            Widget(size_hint_y=None, height="5dp")
        )
        data_tables.ids.container.add_widget(
            MDRaisedButton(
                text="Send Data",
                pos_hint={"right": 1},
                on_release=lambda x: self.send_data_sr(),
            )
        )

        Logger.info(f"Loaded data in {time()-self._start_time:.3} seconds")
        self.view.ids.table_content.clear_widgets()
        self.view.ids.table_content.add_widget(data_tables)
        Logger.info(f"Added to screen in {time()-self._start_time:.3} seconds")

        # self.app.close_loading_screen()

    def on_enter(self):
        Logger.info(f"On enter in {time()-self._start_time:.3} seconds")

    def send_data_sr(self, *args):

        pass

