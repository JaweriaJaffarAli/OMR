from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
import os
from connected import Connected
from connected import Reference
from connected import Answer
from connected import Result
from connected import ImportFile
from connected import ImportFile2
from connected import SelectOpt
from connected import SelectOpt1
from connected import CustomPopup
import re
from Result import login_check
class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        if(loginText == '' or passwordText== '' ):
            obj = CustomPopup()
            obj.call_pops('Fill up please!', 'Some fields are empty!')
        else:
            app.username = loginText
            app.password = passwordText
            found = login_check(loginText , passwordText)
            if found == 1:
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'connected'
            else:
                obj1 = CustomPopup()
                obj1.call_pops('Try Again', 'Wrong ID or password')

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""



class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):

        manager = ScreenManager()
        manager.id = 'parenthere'
        manager.name = 'parenthere'
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Reference(name='reference'))
        manager.add_widget(ImportFile(name='importfile'))
        manager.add_widget(SelectOpt(name='selectopt', id='selectopthere'))
        manager.add_widget(ImportFile2(name='importfile2'))
        manager.add_widget(SelectOpt(name='selectopt1', id='selectopthere1'))
        manager.add_widget(Answer(name='answer'))
        manager.add_widget(Result(name='result'))


        return manager


if __name__ == '__main__':
    LoginApp().run()
