import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
#from kivy.uix.screenmanager import ScreenManager, Screen


#class FirstWindow(Screen):
    #pass


#class SecondWindow(Screen):
    #pass


#class WindowMgr(ScreenManager):
    #FirstWindow()

class Sergiboard(App):
    def build(self):
        return BoxLayout()

if __name__ == "__main__":
    Sergiboard().run()
