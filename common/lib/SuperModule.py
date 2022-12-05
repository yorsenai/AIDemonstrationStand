from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFrame

from common.lib.CallMessageBox import CallMessageBox

import os
import json

class SuperModule(QFrame):
    def __init__(self, demonstration_type : str, slides : int, parent = None, parameters = None):
        super().__init__()
        loadUi(os.path.join('common', 'ui', 'frameDemo.ui'), self)

        self.cwd = os.getcwd()
        self.parent = parent
        self.demonstration_type = demonstration_type # normal || attack || protect
        self.max_slides = slides #Возможно потом не понадобится
        self.parameters = parameters

        self.InfoTextPlate.setReadOnly(True)
        self.ScriptTextPlate.setReadOnly(True)

        self.current_slide = 1

        self.pushButtonMenu.clicked.connect(lambda state = True, 
            button = self.pushButtonMenu : self.SetDemoSlide(state, button))
        self.pushButtonNext.clicked.connect(lambda state = True, 
            button = self.pushButtonNext : self.SetDemoSlide(state, button))
        self.pushButtonBack.clicked.connect(lambda state = True, 
            button = self.pushButtonBack : self.SetDemoSlide(state, button))

    def SetDemoSlide(self, _, button):        
        if 'Далее' in button.text():
            self.current_slide = min(self.max_slides - 1, 
                self.current_slide + 1)
        elif 'Назад' in button.text():
            self.current_slide = max(1, self.current_slide - 1)
        else:     #Меню или Завершить     
            self.cleanup()  
            self.parent.openMenu()
            return
        self.showSlide()


    def readSlide(self):
        path = os.path.join(self.cwd, "texts", self.demonstration_type, "slide_" + str(self.current_slide) + ".json")
        with open(path, "r", encoding = 'utf-8') as file:
            slide = json.load(file)
        return slide

    def showSlide(self):
        slide_params = self.readSlide()

        self.changeInfoText(slide_params['info'])
        self.changeScriptText(slide_params['script'])
        self.executeAction(slide_params['action'])

        if self.current_slide == self.max_slides - 1:
            self.pushButtonNext.setText("Завершить")
            self.showResult()
        else:
            self.pushButtonNext.setText("Далее")


    def changePicture(self, path : str):
        self.imageLabel.setPixmap(QPixmap(path).scaled(320, 330))

    def changeInfoText(self, text : str):
        self.InfoTextPlate.setPlainText(text)
    
    def changeScriptText(self, text : str):
        if(self.ScriptTextPlate.toPlainText().find(text) < 0):
            self.ScriptTextPlate.append(text)
    
    def insertResultHtml(self, check : str, text : str):
        if not check in self.ScriptTextPlate.toPlainText():
            self.ScriptTextPlate.insertHtml(text)
    
    def executeAction(self, action):
        if action.get('MessageBox'):
            CallMessageBox(
                action['MessageBox']
            )
    def showResult(self):
        pass

    def cleanup(self):
        pass