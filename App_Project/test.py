from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 1
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            stars: 3
            source: "images\doch-1.jpg"

        MyTile:
            stars: 3
            source: "images\doch-2.jpg"

        MyTile:
            stars: 3
            source: "images\doch-3.jpg"

        MyTile:
            stars: 3
            source: "images\doch-4.jpg"
            
        MyTile:
            stars: 3
            source: "images\doch-5.jpg"
        
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()