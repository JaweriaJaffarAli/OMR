from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from connected import Connected
from connected import Reference
from connected import Answer
from connected import Result
from connected import ImportFile
from connected import ImportFile2
from connected import SelectOpt
from connected import SelectOpt1

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

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

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)

         )

if __name__ == '__main__':
    LoginApp().run()
