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
from kivy.uix.screenmanager import ScreenManager, Screen

import os
import json

class MainScreen(Screen):
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

class Signupscreen(Screen):
    def register_prof(self,user,pwd,subname,msgbox,reg_but):
        f = open('./log_files/login_details.json','r')
        x = f.read()
        result = json.loads(x)
        result['profs'].append({'name':user,'pass':pwd,'Sub Name':subname})
        f.close()
        f = open('./log_files/login_details.json','w+')
        f.write(json.dumps(result))
        msgbox.text = 'Registered'
        reg_but.disabled = True

class SasApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Signupscreen(name='signup'))
        return sm

if __name__ == '__main__':
    SasApp().run()
