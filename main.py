import kivy
kivy.require('1.9.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from pygments.lexers import CythonLexer
from kivy.uix.codeinput import CodeInput

class Myscreen(BoxLayout):
    def log_prof(self,name,password):
        pass
    def register_prof(self):
        pass

class SasApp(App):
    def build(self):
        return Myscreen()

if __name__ == '__main__':
    SasApp().run()
