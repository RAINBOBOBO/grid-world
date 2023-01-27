from kivy.app import App
from kivy.core.window import Window

from screens.main_menu import MainMenu


class MyApp(App):
    def build(self):
        Window.maximize()
        Window.fullscreen = True
        return MainMenu()


if __name__ == "__main__":
    MyApp().run()
