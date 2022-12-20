import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class PerceptronDialog(object):
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
        self.imageCNN.setObjectName("imagePerceptron")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "Perceptron.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема перцептрона"))

class GANDialog(object):
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
        self.imageCNN.setObjectName("imageGAN")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "GAN.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема работы генеративно-состязательной сети"))

class MLPDialog(object):
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
        self.imageCNN.setObjectName("imageMLP")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "MLP.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Схема работы полносвязной нейронной сети"))

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)

        self.cwd = os.path.join("modules", "GAN")
        if self.demonstration_type == "normal":
            self.changePicture(os.path.join(self.cwd, "pics", "Person.png"))
        else:
            self.changePicture(os.path.join(self.cwd, "pics", "GANPerson.png"))
        self.showSlide()

    def executeAction(self, action):
        super().executeAction(action)
        if action.get("DialogWindow"):
            self.ExecuteDemoDialog(
                action["DialogWindow"]
            )
    
    def ExecuteDemoDialog(self, dialog_type : str):
        if dialog_type == "MLP":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = MLPDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        elif dialog_type == "Perceptron":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = PerceptronDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        elif dialog_type == "GAN":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = GANDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
    

    def showResult(self):
        if self.demonstration_type == "protect":
            text = "<p style='color:#FF0000';> NOT PRESENTED (97%) </p>"
            self.insertResultHtml(check = self.parameters['param1'], text = text)
        elif self.demonstration_type == "attack":
            text = "<p style='color:#FF0000';> Обнаружен человек (92%) </p>"
            self.insertResultHtml(check = "_________", text = text)
        elif self.demonstration_type == "normal":
            text = "<p style='color:#00FF00';> Обнаружен человек (92%) </p>"
            self.insertResultHtml(check = "_________", text = text)