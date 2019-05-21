import kivy
from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.lang import Builder

#kv = Builder


#class FirstWindow(Screen):
    #pass


#class SecondWindow(Screen):
    #pass


#class WindowMgr(ScreenManager):
    #FirstWindow()


"""
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3

        self.btn_1 = Button(text="1", font_size=40, id='01')
        self.btn_1.bind(on_press=self.pressed)
        self.add_widget(self.btn_1)

        self.btn_2 = Button(text="2", font_size=40, id='02')
        self.btn_2.bind(on_press=self.pressed)
        self.add_widget(self.btn_2)

        self.btn_3 = Button(text="3", font_size=40, id='03')
        self.btn_3.bind(on_press=self.pressed)
        self.add_widget(self.btn_3)

        self.btn_4 = Button(text="4", font_size=40, id='04')
        self.btn_4.bind(on_press=self.pressed)
        self.add_widget(self.btn_4)

        self.btn_5 = Button(text="5", font_size=40, id='05')
        self.btn_5.bind(on_press=self.pressed)
        self.add_widget(self.btn_5)

        self.btn_6 = Button(text="6", font_size=40, id='06')
        self.btn_6.bind(on_press=self.pressed)
        self.add_widget(self.btn_6)

        self.btn_7 = Button(text="7", font_size=40, id='07')
        self.btn_7.bind(on_press=self.pressed)
        self.add_widget(self.btn_7)

        self.btn_8 = Button(text="8", font_size=40, id='08')
        self.btn_8.bind(on_press=self.pressed)
        self.add_widget(self.btn_8)

        self.btn_9 = Button(text="9", font_size=40, id='09')
        self.btn_9.bind(on_press=self.pressed)
        self.add_widget(self.btn_9)

        self.btn_10 = Button(text="10", font_size=40, id='010')
        self.btn_10.bind(on_press=self.pressed)
        self.add_widget(self.btn_10)

        self.btn_11 = Button(text="11", font_size=40, id='11')
        self.btn_11.bind(on_press=self.pressed)
        self.add_widget(self.btn_11)

        self.btn_12 = Button(text="12", font_size=40, id='12')
        self.btn_12.bind(on_press=self.pressed)
        self.add_widget(self.btn_12)

    def pressed(self, instance):
        num = instance.id
        print(num)
"""

#class Sergiboard(App):
#    def build(self):
#        return MyGrid()

class Sergiboard(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    Sergiboard().run()
