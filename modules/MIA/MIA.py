import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os


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
            picname = "white_target.png"
        elif self.parameters["param1"]  == "монголоид":
            picname = "asian_target.png"
        else:
            picname = "black_target.png"

        self.cwd = os.path.join("modules", "MIA")
        
        try:
            self.changePicture(os.path.join(self.cwd, "pics", picname))
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
    
    def ExecuteDemoDialog(self, _):
        dialog_app = QtWidgets.QDialog()
        DialogWindow = LSTMDialog()
        DialogWindow.setupUi(dialog_app, self.cwd + "\\pics")
        dialog_app.exec()

    def ExecuteDemoScript(self, _):
        pass
    

    def showResult(self):
        if self.demonstration_type == "attack":
            l = ["европеоид", "монголоид", "негроид"]
            l.remove(self.parameters['param1'])
            text = "<p style='color:#FF0000';>" + l[0] + "</p>"
            self.insertResultHtml(check = l[0], text = text)
        else:
            text = "<p style='color:#00FF00';>" + self.parameters['param1'] + "</p>"
            self.insertResultHtml(check = self.parameters['param1'], text = text)