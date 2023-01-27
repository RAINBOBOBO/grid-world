from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
