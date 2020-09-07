from samwise import pb

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
Button.color=[0,1,1,1]
from kivy.uix.label import Label
Label.color=[1,0,1,1]

from kivy.lang import Builder

res = Builder.load_string('''BoxLayout:
    Label:
        text: 'Left1'
        id: lbl1     
    Label:
        text: 'Left2'
        id: lbl2
    Button:
        text: 'Middle'
        on_touch_down: 
            print('Middle: {}'.format(args[1].pos))
    RelativeLayout:
        on_touch_down: 
            print('Relative: {}'.format(args[1].pos))
        Button:
            text: 'Right'
            on_touch_down: 
                print('Right: {}'.format(args[1].pos))''')


class SimpleApp(App):
    def build(self):
        return res


if __name__ == "__main__":
    SimpleApp().run()
    print("")