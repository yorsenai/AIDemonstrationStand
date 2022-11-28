from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json

class SuperModule():
    def __init__(self, demonstration_type : str, slides : int, parent = None, parameters = None):
        
        self.cwd = ".\\"

        self.parent = parent
        self.demonstration_type = demonstration_type # normal || attack || protect
        self.max_slides = slides #Возможно потом не понадобится
        self.parameters = parameters

        self.current_slide = 0

        self.demoFrame = QtWidgets.QFrame()
        self.demoFrame.setObjectName("demoFrame")
        self.demoFrame.setGeometry(QtCore.QRect(0, 0, 1000, 850))
        self.demoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.demoFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.InfoTextPlate = QtWidgets.QTextEdit(self.demoFrame)
        self.InfoTextPlate.setGeometry(QtCore.QRect(10, 10, 460, 720))
        self.InfoTextPlate.setObjectName("InfoTextPlate")
        self.InfoTextPlate.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InfoTextPlate.setFont(font)

        self.imageLabel = QtWidgets.QLabel(self.demoFrame)
        self.imageLabel.setGeometry(QtCore.QRect(500, 10, 340, 340))
        self.imageLabel.setObjectName("ImageLabel")

        self.ScriptTextPlate = QtWidgets.QTextEdit(self.demoFrame)
        self.ScriptTextPlate.setGeometry(QtCore.QRect(500, 370, 460, 340))
        self.ScriptTextPlate.setObjectName("ScriptTextPlate")
        self.ScriptTextPlate.setReadOnly(True)
        self.ScriptTextPlate.setFont(font)

        self.pushButtonMenu = QtWidgets.QPushButton(self.demoFrame)
        self.pushButtonMenu.setGeometry(QtCore.QRect(450, 760, 90, 30))
        self.pushButtonMenu.setObjectName("pushButton")
        self.pushButtonMenu.clicked.connect(lambda state = True, 
            button = self.pushButtonMenu : self.SetDemoSlide(state, button))

        self.pushButtonNext = QtWidgets.QPushButton(self.demoFrame)
        self.pushButtonNext.setGeometry(QtCore.QRect(560, 760, 90, 30))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonNext.clicked.connect(lambda state = True, 
            button = self.pushButtonNext : self.SetDemoSlide(state, button))

        self.pushButtonBack = QtWidgets.QPushButton(self.demoFrame)
        self.pushButtonBack.setGeometry(QtCore.QRect(340, 760, 90, 30))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonBack.clicked.connect(lambda state = True, 
            button = self.pushButtonBack : self.SetDemoSlide(state, button))

        _translate = QtCore.QCoreApplication.translate
        self.pushButtonMenu.setText(_translate("DemoWindow", "Меню"))
        self.pushButtonNext.setText(_translate("DemoWindow", "Далее"))
        self.pushButtonBack.setText(_translate("DemoWindow", "Назад"))


    #Потом наследовать от parent
    def CallMessageBox(self, text : str):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.setWindowTitle("ATTACK ALERT")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    def SetDemoSlide(self, _, button):        
        if 'Далее' in button.text():
            self.current_slide = min(self.max_slides - 1, 
                self.current_slide + 1)
        elif 'Назад' in button.text():
            self.current_slide = max(0, self.current_slide - 1)
        else:     #Меню или Завершить       
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
        
        if self.current_slide == self.max_slides - 1:
            self.pushButtonNext.setText("Завершить")
        else:
            self.pushButtonNext.setText("Далее")

        self.changeInfoText(slide_params['info'])
        self.changeScriptText(slide_params['script'])
        self.executeAction(slide_params['action'])


    def changePicture(self, path : str):
        self.imageLabel.setPixmap(QtGui.QPixmap(path).scaled(320, 330))

    def changeInfoText(self, text : str):
        self.InfoTextPlate.setPlainText(text)
    
    def changeScriptText(self, text : str):
        if(self.ScriptTextPlate.toPlainText().find(text) < 0):
            self.ScriptTextPlate.append(text)
    
    def executeAction(self, action):
        if action.get('MessageBox'):
            self.CallMessageBox(
                action['MessageBox']
            )