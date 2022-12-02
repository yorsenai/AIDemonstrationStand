import os
import common.lib.SuperModule as SM
from PyQt5.QtWidgets import QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
import numpy as np
from random import randint

def gauss_noise(image, mean=0, var=0.001):
    '''
        Добавить гауссовский шум
                 Среднее значение: среднее
                 Вар: Разнообразие
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out



class CNNDialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1060, 400)

        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setGeometry(QtCore.QRect(370, 5, 320, 30))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(14)
        self.labelImage.setFont(myFont)


        self.imageCNN = QtWidgets.QLabel(Dialog)
        self.imageCNN.setGeometry(QtCore.QRect(10, 40, 1040, 320))
        self.imageCNN.setObjectName("imageCNN")
        self.imageCNN.setPixmap(QtGui.QPixmap(overall_path + "\\CNN.png").scaled(1040, 320))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема работы CNN"))


def noiseattack(image : str, level : str = "low"):
    try:
        img = cv2.imdecode(np.fromfile(image, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        if "high" in level:
            mean = -0.15
        else:
            mean = 0

        noised_img = gauss_noise(img, mean=mean, var = 0.0005)

        new_name = image.replace(".png", "")
        cv2.imencode(".png", noised_img)[1].tofile(new_name + "_out.png")
        return True
    except:
        return False


def addParams():
    values =  ["мужчина", "женщина"]
    combobox = QComboBox()
    combobox.addItems(values)
    return [combobox]

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)
        self.parameters["param1"] += str(randint(1, 3))

        self.cwd = os.path.join("modules", "DeepFool")
        
        try:
            self.changePicture(os.path.join(self.cwd, "pics", self.parameters["param1"] + ".png"))
        except:
            self.changePicture(os.path.join(self.cwd, "pics", "мужчина1.png"))
        self.showSlide()
    

    def executeAction(self, action):
        super().executeAction(action)
        if action.get('Script'):
            self.ExecuteDemoScript(
                action['Script']
            )
        elif action.get("DialogWindow"):
            self.ExecuteDemoDialog(
                action["DialogWindow"]
            )
    
    def ExecuteDemoScript(self, in_data : str):
        try:
            if noiseattack(os.path.join(self.cwd, "pics", self.parameters["param1"] + ".png"), level = in_data):
                self.changePicture(os.path.join(self.cwd, "pics", self.parameters["param1"] + "_out.png"))
        except:
            if noiseattack(os.path.join(self.cwd, "pics", "мужчина1.png"), level = "low"):
                self.changePicture(os.path.join(self.cwd, "pics", "мужчина1_out.png"))
    
    def ExecuteDemoDialog(self, _):
        dialog_app = QtWidgets.QDialog()
        DialogWindow = CNNDialog()
        DialogWindow.setupUi(dialog_app, self.cwd + "\\pics")
        dialog_app.exec()

    def showResult(self):
        if self.demonstration_type == "attack":
            if "мужчина" in self.parameters['param1']:
                text = "<br>[*] Man : 2%<p style='color:#FF0000';>[*] Woman : 97%</p>[*] Not Human : 1%<br>"
            else:
                text = "<br>[*] Woman : 2%<p style='color:#FF0000';>[*] Man : 97%</p>[*] Not Human : 1%<br>"
            #self.changeScriptText(text)
            self.ScriptTextPlate.insertHtml(text)


        else:
            if not ("мужчина" in self.parameters['param1']):
                text = "<br>[*] Man : 2%<p style='color:#00FF00';>[*] Woman : 97%</p>[*] Not Human : 1%<br>"
            else:
                text = "<br>[*] Woman : 2%<p style='color:#00FF00';>[*] Man : 97%</p>[*] Not Human : 1%<br>"
            #self.changeScriptText(text)
            self.ScriptTextPlate.insertHtml(text)

    def cleanup(self):
        for filename in os.listdir(os.path.join(self.cwd, "pics")):
            if "_out.png" in filename:
                os.remove(os.path.join(self.cwd, "pics", filename))
