from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty

class ReactObject(Widget):
    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(1)

    def move(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)

class FirstWidget(Widget):
    count = NumericProperty(0)
    obj = ObjectProperty(None)

    def start(self, dt):
        self.obj.move()
        if (self.obj.y < 0) or (self.obj.y + self.obj.height > self.height):
            self.obj.velocity_y *= -1

        if (self.obj.x < 0) or (self.obj.x + self.obj.width > self.width):
            self.obj.velocity_x *= -1

    def on_touch_move(self, touch):
        pos_x = 0
        pos_y = 0
        print(touch)

        if touch.x + self.obj.width > self.width: 
            pos_x = self.width - self.obj.width
        elif touch.x + self.obj.width < 0:
            pos_x = self.obj.width
        else:
            pos_x = touch.x
        
        if touch.y + self.obj.height > self.height: 
            pos_y = self.height - self.obj.height
        elif touch.y + self.obj.height < 0:
            pos_y = self.obj.height
        else:
            pos_y = touch.y
        
        self.obj.move(pos_x, pos_y)

class FirstApp(App):
    def build(self):
        w = FirstWidget()
        #Clock.schedule_interval(w.start, 1.0 / 60.0)
        return w

if __name__=="__main__":
    FirstApp().run()