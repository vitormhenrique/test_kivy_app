from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.lang import Builder

Builder.load_file("libs/kv/login.kv")

class LoginScreen(Screen):

    def login(self, username, password):
        self.manager.transition = CardTransition(direction='down')
        self.manager.current = 'home'