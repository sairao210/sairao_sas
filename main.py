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
from website import*
import threading
import datetime
import urllib2
import time
import os,sys
import json

# global stu_flag
stu_flag = False

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

                    conn = sqlite3.connect('./DataBase/attendance.db')
                    now = datetime.datetime.now()
                    date = str(now.date())
                    cur = conn.cursor()
                    try:
                        cur.execute('ALTER TABLE example ADD '+'['+date+']'+' INTEGER DEFAULT 0')
                        print 'added todays column as '+date
                    except Exception, e:
                        print e
                        pass
                    conn.commit()
                    wel.text = "Logged in as " + item['name']
                else:
                    wel.text =  "Password doesnt match"

        if(flag == 0):
            wel.text =  "Username doesnt match"
        f.close()

    def print_details(self,stu_text):
        conn = sqlite3.connect("./DataBase/attendance.db")
        c = conn.cursor()
        now = datetime.datetime.now()
        date = str(now.date())
        while(1):
            if(stu_flag == True):
                break
            time.sleep(2)
            st = ''
            for row in c.execute("SELECT roll FROM example WHERE "+'['+date+']'+"=?", (1,)):
                for item in row:
                    st+=str(item)+'\t'
                st+='\n'
            # print st
            stu_text.text = st


    def start_server(self,but,txt,stu_text):
        mythread = threading.Thread(target = self.print_details,args=(stu_text,))

        if(but.text == 'Stop server'):
            response = urllib2.urlopen('http://localhost:8080/shutdown')
            txt.text = 'Press above Button to Host attendance website'
            but.text = 'Start server'
            stu_flag = True
            # mythread.join()
        else:
            but.text = 'Stop server'
            threading.Thread(target = serv1,args=('sai',)).start()
            txt.text = 'Server Started'
            stu_flag = False
            # mythread.daemon = True
            mythread.start()



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
