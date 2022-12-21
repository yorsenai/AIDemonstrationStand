import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class DefenseDialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 600)

        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setGeometry(QtCore.QRect(20, 5, 1000, 30))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(12)
        self.labelImage.setFont(myFont)


        self.imageCNN = QtWidgets.QLabel(Dialog)
        self.imageCNN.setGeometry(QtCore.QRect(30, 40, 1000, 526))
        self.imageCNN.setObjectName("imageDefense")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "Defense.png")).scaled(1000, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Защита гиперпараметров"))


class AlgoDialog(object):
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
        self.imageCNN.setObjectName("imageAlgo")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "Algo.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Алгоритм кражи гиперпараметров"))


class FormulesDialog(object):
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
        self.imageCNN.setObjectName("imageFormules")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "Formules.png")).scaled(671, 526))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Рабочие формулы"))


class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)

        self.cwd = os.path.join("modules", "ModelStealing")
        self.showSlide()

    def executeAction(self, action):
        super().executeAction(action)
        if action.get('Script'):
            self.ExecuteDemoScript(
                action['Script']
            )
        if action.get("DialogWindow"):
            self.ExecuteDemoDialog(
                action["DialogWindow"]
            )
        
    def ExecuteDemoScript(self, param):
        if param == "LASSO":
            self.changePicture(os.path.join(self.cwd, "pics", "LASSO.png"))
        elif param == "HYPER":
            self.changePicture(os.path.join(self.cwd, "pics", "Hyper.png"))
        elif param == "normal":
            pass
    
    
    def ExecuteDemoDialog(self, dialog_type : str):
        if dialog_type == "FORMULES":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = FormulesDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        if dialog_type == "ALGO":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = AlgoDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
        if dialog_type == "DEFENSE":
            dialog_app = QtWidgets.QDialog()
            DialogWindow = DefenseDialog()
            
            DialogWindow.setupUi(dialog_app,  os.path.join(self.cwd, "pics"))
            dialog_app.exec()
    
    

    def showResult(self):
        pass