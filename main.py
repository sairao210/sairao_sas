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
import os
import json
class Myscreen(BoxLayout):
    def log_prof(self,name,password,wel,sign_in):
        f = open('./log_files/login_details.json',"r")
        x = f.read()
        result = json.loads(x)
        flag = 0

        for item in result['profs']:
            if(name == item['name'] and flag==0):
                flag = 1
                if(password == item['pass']):
                    wel.text = "Logged in as " + item['name']
                else:
                    wel.text =  "Password doesnt match"

        if(flag == 0):
            wel.text =  "Username doesnt match"

        f.close()
    def register_prof(self):
        pass

class SasApp(App):
    def build(self):
        return Myscreen()

if __name__ == '__main__':
    SasApp().run()
