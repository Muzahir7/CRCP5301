from kivymd.app import MDApp
from kivymd.theming import ThemeManager

class MainApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        pass

MainApp().run()