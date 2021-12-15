from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Increment(Widget):

    def inc(self):
        self.count = self.count + 1 

class FirstApp(App):
    pass

if __name__=="__main__":
    FirstApp().run()