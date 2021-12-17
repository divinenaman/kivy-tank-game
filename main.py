from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window

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

    def move_on_keypress(self, **touch):
        pos_x = 0
        pos_y = 0

        if touch['x'] + self.obj.width > self.width: 
            pos_x = self.width - self.obj.width
        elif touch['x'] < 0:
            pos_x = 0
        else:
            pos_x = touch['x']
        
        if touch['y'] + self.obj.height > self.height: 
            pos_y = self.height - self.obj.height
        elif touch['y'] < 0:
            pos_y = 0
        else:
            pos_y = touch['y']
        
        self.obj.move(pos_x, pos_y)

class FirstApp(App):
    def build(self):
        self.widget = FirstWidget()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        #Clock.schedule_interval(w.start, 1.0 / 60.0)
        return self.widget
    
    def _keyboard_closed(self):
            self._keyboard.unbind(on_key_down=self._on_keyboard_down)
            self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        k = keycode[1]
        
        if k == 'right':
            self.widget.move_on_keypress(x=self.widget.obj.x + 3, y=self.widget.obj.y)
        if k == 'left':
            self.widget.move_on_keypress(x=self.widget.obj.x - 3, y=self.widget.obj.y)
        if k == 'up':
            self.widget.move_on_keypress(x=self.widget.obj.x, y=self.widget.obj.y + 3)
        if k == 'down':
            self.widget.move_on_keypress(x=self.widget.obj.x, y=self.widget.obj.y - 3) 
        
        return True 

if __name__=="__main__":
    FirstApp().run()