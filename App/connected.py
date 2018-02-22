from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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

ans = []
score = 0
imag = 0
imagLoc =0
paper = 0
path = 0
RollNumber = 0
class Reference(Screen):
   pass


class Answer(Screen):
    def EnterRollNo(self, RollNo):
        global RollNumber
        RollNumber = RollNo

class Result(Screen,GridLayout):
    def PrintResult(self):
        res = " "
        res = str(score)
        return res

    def ShowPaper(self):
        paper , score = AnswerSheet.AnswerSheet(self, imag, ans)
        print(score)
        self.ids.Pimage.source = imagLoc
        self.ids['rollno'].text = str(RollNumber)
        self.ids['Score'].text = str(score)


image_here = None
class ImportFile(Screen, BoxLayout):
    global path1

    def selected(self,filename):
        self.ids.image.source = filename[0]

    def open(self , filename, path):
        #GridLayout1.Display(filename[0])
        global ans , a

        img = cv2.imread(filename[0])
        global image_here
        image_here = filename[0]
        ans = ReferenceSheet.capturerefsheet(self, img)
        print(ans)
        self.manager.current = 'selectopt'
        print(self.parent)
        print(self.parent.get_screen('selectopt').ids)
        self.parent.get_screen('selectopt').ids['image'].source = filename[0]


    def getName(self):
        return self.path1

class SelectOpt(Screen):

    def __init(self, **kwargs):
        super(self,Screen).__init__(self, **kwargs)
        global image_here
        print(self.ids)
        self.ids['image'] = image_here

    def Display(self,filename):
        self.manager.current = 'selectopt'
        self.ids.Dimage.source = filename[0]

class SelectOpt1(Screen):

    def __init(self, **kwargs):
        super(self,Screen).__init__(self, **kwargs)
        global image_here
        print(self.ids)
        self.ids['image'] = image_here

    def Display(self,filename):
        self.manager.current = 'selectopt'
        self.ids.Dimage.source = filename[0]
class ImportFile2(Screen, BoxLayout):
    def selected(self,filename):
        self.ids.Aimage.source = filename[0]
    def ImportAns(self,filename, path):
        global score , imag, imagLoc
        imag = cv2.imread(filename[0])
        imagLoc = filename[0]
        self.manager.current = 'selectopt1'