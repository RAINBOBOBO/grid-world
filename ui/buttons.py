from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_press = self.close_app

    def close_app(self):
        App.get_running_app().stop()
        Window.close()
