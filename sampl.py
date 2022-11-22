from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT,'ヒラギノ角ゴシック W0.ttc')

class TextApp(App):
    def build(self):
        return Label(text='みなさん、こんにちわ。')

TextApp().run()