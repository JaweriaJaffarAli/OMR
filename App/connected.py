from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
import numpy as np
import cv2
from transform import four_point_transform
import imutils
from imutils import contours
from imutils.perspective import four_point_transform
import argparse
import string
from ReferenceSheet import ReferenceSheet
from AnswerSheet import AnswerSheet

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
    def dismiss(self):
        App.get_running_app().stop()
    def CheckRefSheet(self):
        if image_here == None:
            print('Select Reference Sheet first')
            obj= CustomPopup()
            obj.call_pops('Reference Sheet Missing!', 'Add Reference Sheet First!')
        else:
            self.manager.current = 'answer'
class CustomPopup(Popup):
    def call_pops(self,tit,conten):
        cont=Button(text=conten)
        pop=Popup(title=tit,content=cont,size_hint=(None, None), size=(250, 150),auto_dismiss=True)
        pop.open()
        cont.bind(on_press=pop.dismiss)
ans = []
score = 0
imag = 0
img = 0
paper = 0
path = 0
RollNumber = 0
image_here = None
image_here2 = None
class Reference(Screen):
    def dismiss(self):
        App.get_running_app().stop()


class Answer(Screen):
    def EnterRollNo(self, RollNo):
        global RollNumber
        if(len(RollNo) <= 4 or len(RollNo) > 5):
            self.ids['rollNo'].text = ""
            obj = CustomPopup()
            obj.call_pops('Fill up again!', '5 Digit Roll No is Required')
        else:
            RollNumber = RollNo
    def dismiss(self):
        App.get_running_app().stop()
    def Check_RollNumber(self):
        global RollNumber
        if RollNumber == 0:
            obj= CustomPopup()
            obj.call_pops('Fill up please!','Some fields are empty!')
        else:
            self.manager.current = 'importfile2'
class Result(Screen,GridLayout):
    def dismiss(self):
        App.get_running_app().stop()

    def ShowPaper(self):
        if image_here2 == None:
            print('Select Answer Sheet first')
            obj = CustomPopup()
            obj.call_pops('Answer Sheet Missing!', 'Add Answer Sheet!')

        else:
            paper , score = AnswerSheet.AnswerSheet(self, imag, ans)
            print(score)
            self.ids.Pimage.source = image_here2
            self.ids['rollno'].text = str(RollNumber)
            self.ids['Score'].text = str(score)

class ImportFile(Screen, BoxLayout):
    global path1

    def selected(self,filename):
        self.ids.image.source = filename[0]

    def open(self , filename, path):

        global ans , a ,img

        img = cv2.imread(filename[0])
        global image_here
        image_here = filename[0]
        ans = ReferenceSheet.capturerefsheet(self, img)
        print(ans)
        self.manager.current = 'selectopt'
        self.parent.get_screen('selectopt').ids['image'].source = filename[0]


    def getName(self):
        return self.path1

class SelectOpt(Screen):
    def Display(self,filename):
        self.manager.current = 'selectopt'
        self.ids.Dimage.source = filename[0]

class SelectOpt1(Screen):
    def Display(self,filename):
        self.manager.current = 'selectopt'
        self.ids.Dimage.source = filename[0]
class ImportFile2(Screen, BoxLayout):
    def selected(self,filename):
        self.ids.Aimage.source = filename[0]
    def ImportAns(self,filename, path):
        global score , imag, image_here2
        imag = cv2.imread(filename[0])
        image_here2 = filename[0]
        self.manager.current = 'selectopt1'
        self.parent.get_screen('selectopt1').ids['image'].source = filename[0]