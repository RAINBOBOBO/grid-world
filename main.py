from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

builder = Builder.load_file("ui/designs/screen_manager.kv")


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.maximize()
        Window.fullscreen = True

    def build(self):
        return builder


if __name__ == "__main__":
    MyApp().run()
