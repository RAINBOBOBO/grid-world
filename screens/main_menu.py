from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MainMenu(GridLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.add_widget(Button(text="Start"))
        self.add_widget(Button(text="Settings"))

        self.quit = Button(text="Quit")
        self.quit.bind(on_press=self.close_app)
        self.add_widget(self.quit)

    def close_app(self, button):
        App.get_running_app().stop()
        Window.close()
