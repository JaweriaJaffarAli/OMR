from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'login id'
        Button:
            text: 'password'
        Button:
            text: 'Login'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press: root.dismiss()

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'capture reference sheet'
            
        Button:
            text: 'capture answer sheet'
        Button:
            text: 'capture reference sheet'
        Button:
            text: 'view result'
        Button:
            text: 'Quit'
            on_press: root.dismiss()

""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
class Screen_Change(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Screen_Change().run()
name = 2
print (name.title())
