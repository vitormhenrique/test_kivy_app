from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
#: import Clock kivy.clock.Clock

<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDBoxLayout:
        orientation: "horizontal"
        adaptive_height: False
        spacing: "10dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            font_style: "Body1"
            text: "Toggle to set custom panel color"
            halign: "center"

        MDSwitch:
            size_hint: None, None
            size: "36dp", "48dp"
            pos_hint: {"center_x": .5}

    MDTextField:
        hint_text: "City"
        text: "test"
        on_focus: Clock.schedule_once(lambda dt: self.select_all(), 0.2) if self.focus else None


MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''


class Content(BoxLayout):
    pass


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()


Example().run()