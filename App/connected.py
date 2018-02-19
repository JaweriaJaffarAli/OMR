from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
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
paper = 0
class Reference(Screen):
    def ImportRef(self):
        global ans
        img = cv2.imread('F:\PyCharm Community Edition 2017.2/Projects/optical-mark-recognition/images/test_03.png')
        ans = ReferenceSheet.capturerefsheet(self, img)
        self.manager.current = 'connected'


class Answer(Screen):
    def ImportAns(self):
        global score , imag
        imag = cv2.imread('F:\PyCharm Community Edition 2017.2/Projects/optical-mark-recognition/images/test_02.png')
        self.manager.current = 'connected'

class Result(Screen):
    def PrintResult(self):
        return score
    def ShowPaper(self):
        AnswerSheet.AnswerSheet(self, imag, ans)

class ImportFile(Screen, BoxLayout):
    path1 = string
    def selected(self,filename):
        self.ids.image.source = filename[0]
    def open(self, filename):
        self.path1 = str(filename)
        CalcGridLayout.Display(filename[0])


    def getName(self):
        return self.path1
class CalcGridLayout(Screen):
    def Display(self, filename):
        self.ids.Dimage.source = filename[0]