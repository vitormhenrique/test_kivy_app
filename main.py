"""
SRMobile
=============


"""

import os
import sys
from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

from libs.baseclass.home import HomeScreen
from libs.baseclass.login import LoginScreen


def get_session():
    return False

class SRMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "SR Mobile"

    def build(self):
        manager = ScreenManager()
        if get_session() is False:
            manager.add_widget(LoginScreen(name='login'))
            manager.add_widget(HomeScreen(name='home'))
            manager.current = 'login'
        else:
            manager.add_widget(HomeScreen(name='home'))
            manager.add_widget(LoginScreen(name='login'))
            manager.current = 'home'

SRMobile().run()
