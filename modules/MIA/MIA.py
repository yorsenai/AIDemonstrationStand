from random import randint
import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class ShadowDialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 820)

        self.labelDataSet = QtWidgets.QLabel(Dialog)
        self.labelDataSet.setGeometry(QtCore.QRect(130, 5, 320, 30))
        self.labelDataSet.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDataSet.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(14)
        self.labelDataSet.setFont(myFont)
        myFont.setPointSize(9)



        self.frameWHITE = QtWidgets.QFrame(Dialog)
        self.frameWHITE.setGeometry(QtCore.QRect(10, 30, 560, 240))
        self.frameWHITE.setMinimumSize(QtCore.QSize(400, 360))
        self.frameWHITE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWHITE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWHITE.setObjectName("frameWHITE")

        self.imageWHITE = QtWidgets.QLabel(self.frameWHITE)
        self.imageWHITE.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageWHITE.setObjectName("imageWHITE1")
        #self.imageWHITE.setPixmap(QtGui.QPixmap(overall_path + "\\white.png").scaled(180, 160))


        self.labelWhite = QtWidgets.QLabel(self.frameWHITE)
        self.labelWhite.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelWhite.setAlignment(QtCore.Qt.AlignLeft)
        self.labelWhite.setObjectName("labelWhite")
        self.labelWhite.setFont(myFont)


        self.frameBLACK = QtWidgets.QFrame(Dialog)
        self.frameBLACK.setGeometry(QtCore.QRect(10, 300, 560, 240))
        self.frameBLACK.setMinimumSize(QtCore.QSize(400, 360))
        self.frameBLACK.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBLACK.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBLACK.setObjectName("frameBLACK")

        self.imageBLACK = QtWidgets.QLabel(self.frameBLACK)
        self.imageBLACK.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageBLACK.setObjectName("imageBLACK1")
        #self.imageBLACK.setPixmap(QtGui.QPixmap(overall_path + "\\black.png").scaled(180, 160))

        self.labelBlack = QtWidgets.QLabel(self.frameBLACK)
        self.labelBlack.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelBlack.setAlignment(QtCore.Qt.AlignLeft)
        self.labelBlack.setObjectName("labelBlack")
        self.labelBlack.setFont(myFont)



        self.frameASIAN = QtWidgets.QFrame(Dialog)
        self.frameASIAN.setGeometry(QtCore.QRect(10, 570, 560, 240))
        self.frameASIAN.setMinimumSize(QtCore.QSize(400, 360))
        self.frameASIAN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameASIAN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameASIAN.setObjectName("frameASIAN")

        self.imageASIAN = QtWidgets.QLabel(self.frameASIAN)
        self.imageASIAN.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageASIAN.setObjectName("imageASIAN1")
        #self.imageASIAN.setPixmap(QtGui.QPixmap(overall_path + "\\asian.png").scaled(180, 160))


        self.labelAsian = QtWidgets.QLabel(self.frameASIAN)
        self.labelAsian.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelAsian.setAlignment(QtCore.Qt.AlignLeft)
        self.labelAsian.setObjectName("labelAsian")
        self.labelAsian.setFont(myFont)

        

        self.set_pictures(path = overall_path)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_pictures(self, path):
        self.imageWHITE.setPixmap(QtGui.QPixmap(path + "\\white2.png").scaled(380, 220))
        self.imageBLACK.setPixmap(QtGui.QPixmap(path + "\\black1.png").scaled(380, 220))
        self.imageASIAN.setPixmap(QtGui.QPixmap(path + "\\asian1.png").scaled(380, 220))
        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.labelWhite.setText(_translate("Dialog", "Негроид: 0.01;\nЕвропеоид: 0.94;\nМонголоид: 0.05;"))
        self.labelBlack.setText(_translate("Dialog", "Негроид: 0.95;\nЕвропеоид: 0.04;\nМонголоид: 0.01;"))
        self.labelAsian.setText(_translate("Dialog", "Негроид: 0.02;\nЕвропеоид: 0.04;\nМонголоид: 0.94;"))
        self.labelDataSet.setText(_translate("Dialog", "Обучающий набор данных"))


class PresidentDialog(object):
    def setupUi(self, Dialog, overall_path : str, target_race : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 820)

        self.labelDataSet = QtWidgets.QLabel(Dialog)
        self.labelDataSet.setGeometry(QtCore.QRect(130, 5, 320, 30))
        self.labelDataSet.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDataSet.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(14)
        self.labelDataSet.setFont(myFont)
        myFont.setPointSize(9)



        self.frameWHITE = QtWidgets.QFrame(Dialog)
        self.frameWHITE.setGeometry(QtCore.QRect(10, 30, 560, 240))
        self.frameWHITE.setMinimumSize(QtCore.QSize(400, 360))
        self.frameWHITE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWHITE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWHITE.setObjectName("frameWHITE")

        self.imageWHITE = QtWidgets.QLabel(self.frameWHITE)
        self.imageWHITE.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageWHITE.setObjectName("imageWHITE1")
        #self.imageWHITE.setPixmap(QtGui.QPixmap(overall_path + "\\white.png").scaled(180, 160))


        self.labelWhite = QtWidgets.QLabel(self.frameWHITE)
        self.labelWhite.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelWhite.setAlignment(QtCore.Qt.AlignLeft)
        self.labelWhite.setObjectName("labelWhite")
        self.labelWhite.setFont(myFont)


        self.frameBLACK = QtWidgets.QFrame(Dialog)
        self.frameBLACK.setGeometry(QtCore.QRect(10, 300, 560, 240))
        self.frameBLACK.setMinimumSize(QtCore.QSize(400, 360))
        self.frameBLACK.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBLACK.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBLACK.setObjectName("frameBLACK")

        self.imageBLACK = QtWidgets.QLabel(self.frameBLACK)
        self.imageBLACK.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageBLACK.setObjectName("imageBLACK1")
        #self.imageBLACK.setPixmap(QtGui.QPixmap(overall_path + "\\black.png").scaled(180, 160))

        self.labelBlack = QtWidgets.QLabel(self.frameBLACK)
        self.labelBlack.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelBlack.setAlignment(QtCore.Qt.AlignLeft)
        self.labelBlack.setObjectName("labelBlack")
        self.labelBlack.setFont(myFont)



        self.frameASIAN = QtWidgets.QFrame(Dialog)
        self.frameASIAN.setGeometry(QtCore.QRect(10, 570, 560, 240))
        self.frameASIAN.setMinimumSize(QtCore.QSize(400, 360))
        self.frameASIAN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameASIAN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameASIAN.setObjectName("frameASIAN")

        self.imageASIAN = QtWidgets.QLabel(self.frameASIAN)
        self.imageASIAN.setGeometry(QtCore.QRect(10, 10, 380, 220))
        self.imageASIAN.setObjectName("imageASIAN1")
        #self.imageASIAN.setPixmap(QtGui.QPixmap(overall_path + "\\asian.png").scaled(180, 160))


        self.labelAsian = QtWidgets.QLabel(self.frameASIAN)
        self.labelAsian.setGeometry(QtCore.QRect(400, 10, 140, 220))
        self.labelAsian.setAlignment(QtCore.Qt.AlignLeft)
        self.labelAsian.setObjectName("labelAsian")
        self.labelAsian.setFont(myFont)

        

        self.set_pictures(path = overall_path, race = target_race)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_pictures(self, path, race):
        i = str(randint(1,2))
        print(path + "\\white" + i + ".png")
        if race == "white":
            self.imageWHITE.setPixmap(QtGui.QPixmap(path + "\\white_target.png").scaled(380, 220))
            self.imageBLACK.setPixmap(QtGui.QPixmap(path + "\\black" + i + ".png").scaled(380, 220))
            self.imageASIAN.setPixmap(QtGui.QPixmap(path + "\\asian" + i + ".png").scaled(380, 220))
        elif race == "black":
            self.imageWHITE.setPixmap(QtGui.QPixmap(path + "\\white2.png").scaled(380, 220))
            self.imageBLACK.setPixmap(QtGui.QPixmap(path + "\\black_target.png").scaled(380, 220))
            self.imageASIAN.setPixmap(QtGui.QPixmap(path + "\\asian" + i + ".png").scaled(380, 220))
        elif race == "asian":
            self.imageWHITE.setPixmap(QtGui.QPixmap(path + "\\white" + i + ".png").scaled(380, 220))
            self.imageBLACK.setPixmap(QtGui.QPixmap(path + "\\black" + i + ".png").scaled(380, 220))
            self.imageASIAN.setPixmap(QtGui.QPixmap(path + "\\asian_target.png").scaled(380, 220))
        else:
            return


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.labelWhite.setText(_translate("Dialog", "Негроид: 0.01;\nЕвропеоид: 0.94;\nМонголоид: 0.05;"))
        self.labelBlack.setText(_translate("Dialog", "Негроид: 0.95;\nЕвропеоид: 0.04;\nМонголоид: 0.01;"))
        self.labelAsian.setText(_translate("Dialog", "Негроид: 0.02;\nЕвропеоид: 0.04;\nМонголоид: 0.94;"))
        self.labelDataSet.setText(_translate("Dialog", "Обучающий набор данных"))

class MIADialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(810, 600)

        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setGeometry(QtCore.QRect(20, 5, 751, 30))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(12)
        self.labelImage.setFont(myFont)


        self.imageCNN = QtWidgets.QLabel(Dialog)
        self.imageCNN.setGeometry(QtCore.QRect(30, 40, 751, 526))
        self.imageCNN.setObjectName("imageMIA")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "MIA.png")).scaled(751, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема работы атаки вывода членства"))


class LSTMDialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 600)

        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setGeometry(QtCore.QRect(20, 5, 671, 30))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(12)
        self.labelImage.setFont(myFont)


        self.imageCNN = QtWidgets.QLabel(Dialog)
        self.imageCNN.setGeometry(QtCore.QRect(30, 40, 671, 526))
        self.imageCNN.setObjectName("imageLSTM")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "LSTM.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема работы LSTM-сети"))


def addParams():
    values =  ["европеоид", "негроид", "монголоид"]
    combobox = QtWidgets.QComboBox()
    combobox.addItems(values)
    return [combobox]

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)

        

        if self.parameters["param1"]  == "европеоид":
            self.target = "white"
        elif self.parameters["param1"]  == "монголоид":
            self.target = "asian"
        else:
            self.target = "black"

        self.cwd = os.path.join("modules", "MIA")
        self.picname = self.target + "_target.png"
        try:
            self.changePicture(os.path.join(self.cwd, "pics", self.picname))
        except:
            self.changePicture(os.path.join(self.cwd, "pics", "asian_target.png"))

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
    
    def ExecuteDemoDialog(self, dialog_type):
        if dialog_type == "LTSM":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = LSTMDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        elif dialog_type == "MIA":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = MIADialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        elif dialog_type == "SHADOW":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = ShadowDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        elif dialog_type == "PRESIDENT":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = PresidentDialog()
            DialogWindow.setupUi(dialog_app, overall_path = os.path.join(self.cwd, "pics"), target_race = self.target)
            dialog_app.exec()

    def ExecuteDemoScript(self, param):
        if param == "LSTM":
            if self.target == "white":
                self.ScriptTextPlate.append("Негроид: 0.01;\nЕвропеоид: 0.94;\nМонголоид: 0.05;")
            elif self.target == "asian":
                self.ScriptTextPlate.append("Негроид: 0.02;\nЕвропеоид: 0.04;\nМонголоид: 0.94;")
            elif self.target == "black":
                self.ScriptTextPlate.append("Негроид: 0.95;\nЕвропеоид: 0.04;\nМонголоид: 0.01;")
    

    def showResult(self):
        if self.demonstration_type == "defense":
            l = ["европеоид", "монголоид", "негроид"]
            l.remove(self.parameters['param1'])
            text = "<p style='color:#FF0000';>" + l[0] + "</p>"
            self.insertResultHtml(check = l[0], text = text)
        elif self.demonstration_type == "attack":
            text = "<p style='color:#00FF00';>" + self.parameters['param1'] + ": 0.963" + "</p>"
            self.insertResultHtml(check = self.parameters['param1'], text = text)
        else:
            text = "<p style='color:#00FF00';>" + self.parameters['param1'] + "</p>"
            self.insertResultHtml(check = self.parameters['param1'], text = text)