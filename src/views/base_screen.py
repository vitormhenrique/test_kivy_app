from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from utility.observer import Observer
from kivy.clock import Clock
from functools import partial
from kivy.logger import Logger

class BaseScreenView(ThemableBehavior, MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data
    :class:`~Model.coffe_concept_screen.CoffeConceptScreenModel`.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.coffe_concept_screen.CoffeConceptScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.coffe_concept_screen.CoffeConceptScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    screen_manager = ObjectProperty()
    """
    Screen manager object - :class:`~kivy.uix.screenmanager.ScreenManager`.

    :attr:`screen_manager` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    app = ObjectProperty()

    def goto_screen(self, screen_name):
        self.controller.transition_to_screen(screen_name)

        
    def on_pre_enter(self):
        # self.app.start_loading_screen()
        invert_op = getattr(self.controller, "on_pre_enter", None)
        Logger.debug('on_pre_enter called')
        if callable(invert_op):
            invert_op()

    def on_enter(self):
        invert_op = getattr(self.controller, "on_enter", None)
        Logger.debug('on_enter called')
        if callable(invert_op):
            invert_op()

    def on_leave(self):
        self.app.close_loading_screen()
        invert_op = getattr(self.controller, "on_leave", None)
        Logger.debug('on_leave called')
        if callable(invert_op):
            invert_op()

    def on_pre_leave(self):
        invert_op = getattr(self.controller, "on_pre_leave", None)
        Logger.debug('on_pre_leave called')
        if callable(invert_op):
            invert_op()

    def __init__(self, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        if self.model is not None:
            self.model.add_observer(self)
