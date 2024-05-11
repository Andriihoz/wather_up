from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDscreen

class MainScreen(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class WatherApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.screen = MainScreen('main_screen')
        return MDLabel(text="Hello, World", halign="center")


MainApp().run()