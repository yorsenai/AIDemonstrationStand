import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class SignDialog(object):
    def setupUi(self, Dialog, overall_path : str, atk : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(880, 820)

        self.labelDataSet = QtWidgets.QLabel(Dialog)
        self.labelDataSet.setGeometry(QtCore.QRect(280, 5, 320, 30))
        self.labelDataSet.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDataSet.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(14)
        self.labelDataSet.setFont(myFont)


        self.frameSTOP = QtWidgets.QFrame(Dialog)
        self.frameSTOP.setGeometry(QtCore.QRect(10, 30, 400, 360))
        self.frameSTOP.setMinimumSize(QtCore.QSize(400, 360))
        self.frameSTOP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSTOP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSTOP.setObjectName("frameSTOP")

        self.imageSTOP1 = QtWidgets.QLabel(self.frameSTOP)
        self.imageSTOP1.setGeometry(QtCore.QRect(10, 10, 180, 160))
        self.imageSTOP1.setObjectName("imageSTOP1")
        self.imageSTOP1.setPixmap(QtGui.QPixmap(overall_path + "\\stop1.png").scaled(180, 160))

        self.imageSTOP2 = QtWidgets.QLabel(self.frameSTOP)
        self.imageSTOP2.setGeometry(QtCore.QRect(10, 190, 180, 160))
        self.imageSTOP2.setObjectName("imageSTOP2")
        self.imageSTOP2.setPixmap(QtGui.QPixmap(overall_path + "\\stop2.png").scaled(180, 160))

        self.imageSTOP3 = QtWidgets.QLabel(self.frameSTOP)
        self.imageSTOP3.setGeometry(QtCore.QRect(210, 10, 180, 160))
        self.imageSTOP3.setObjectName("imageSTOP3")
        self.imageSTOP3.setPixmap(QtGui.QPixmap(overall_path + "\\stop3.png").scaled(180, 160))

        self.imageSTOP4 = QtWidgets.QLabel(self.frameSTOP)
        self.imageSTOP4.setGeometry(QtCore.QRect(210, 190, 180, 160))
        self.imageSTOP4.setObjectName("imageSTOP4")
        self.imageSTOP4.setPixmap(QtGui.QPixmap(overall_path + "\\stop4.png").scaled(180, 160))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 380, 80, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")




        self.frameSPEED = QtWidgets.QFrame(Dialog)
        self.frameSPEED.setGeometry(QtCore.QRect(470, 30, 400, 360))
        self.frameSPEED.setMinimumSize(QtCore.QSize(400, 360))
        self.frameSPEED.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSPEED.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSPEED.setObjectName("frameSPEED")

        self.imageSPEED1 = QtWidgets.QLabel(self.frameSPEED)
        self.imageSPEED1.setGeometry(QtCore.QRect(10, 10, 180, 160))
        self.imageSPEED1.setObjectName("imageSPEED1")
        self.imageSPEED1.setPixmap(QtGui.QPixmap(overall_path + "\\speed1.png").scaled(180, 160))

        self.imageSPEED2 = QtWidgets.QLabel(self.frameSPEED)
        self.imageSPEED2.setGeometry(QtCore.QRect(10, 190, 180, 160))
        self.imageSPEED2.setObjectName("imageSPEED2")
        self.imageSPEED2.setPixmap(QtGui.QPixmap(overall_path + "\\speed2.png").scaled(180, 160)) 

        self.imageSPEED3 = QtWidgets.QLabel(self.frameSPEED)
        self.imageSPEED3.setGeometry(QtCore.QRect(210, 10, 180, 160))
        self.imageSPEED3.setObjectName("imageSPEED3")
        if atk == "attack":
            self.imageSPEED3.setStyleSheet("border: 5px solid red;")
            self.imageSPEED3.setPixmap(QtGui.QPixmap(overall_path + "\\speed3_atk.png").scaled(180, 160))
        else:
            self.imageSPEED3.setPixmap(QtGui.QPixmap(overall_path + "\\speed3.png").scaled(180, 160))

        self.imageSPEED4 = QtWidgets.QLabel(self.frameSPEED)
        self.imageSPEED4.setGeometry(QtCore.QRect(210, 190, 180, 160))
        self.imageSPEED4.setObjectName("imageSPEED4")
        self.imageSPEED4.setPixmap(QtGui.QPixmap(overall_path + "\\speed4.png").scaled(180, 160))

        self.labelSpeed = QtWidgets.QLabel(Dialog)
        self.labelSpeed.setGeometry(QtCore.QRect(580, 380, 160, 20))
        self.labelSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed.setObjectName("labelSpeed")



        self.frameCROSS = QtWidgets.QFrame(Dialog)
        self.frameCROSS.setGeometry(QtCore.QRect(470, 410, 400, 360))
        self.frameCROSS.setMinimumSize(QtCore.QSize(400, 360))
        self.frameCROSS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCROSS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCROSS.setObjectName("frameCROSS")

        self.imageCROSS1 = QtWidgets.QLabel(self.frameCROSS)
        self.imageCROSS1.setGeometry(QtCore.QRect(10, 10, 180, 160))
        self.imageCROSS1.setObjectName("imageCROSS1")
        self.imageCROSS1.setPixmap(QtGui.QPixmap(overall_path + "\\cross1.png").scaled(180, 160))

        self.imageCROSS2 = QtWidgets.QLabel(self.frameCROSS)
        self.imageCROSS2.setGeometry(QtCore.QRect(10, 190, 180, 160))
        self.imageCROSS2.setObjectName("imageCROSS2")
        self.imageCROSS2.setPixmap(QtGui.QPixmap(overall_path + "\\cross2.png").scaled(180, 160))
        

        self.imageCROSS3 = QtWidgets.QLabel(self.frameCROSS)
        self.imageCROSS3.setGeometry(QtCore.QRect(210, 10, 180, 160))
        self.imageCROSS3.setObjectName("imageCROSS3")
        self.imageCROSS3.setPixmap(QtGui.QPixmap(overall_path + "\\cross3.png").scaled(180, 160))


        self.imageCROSS4 = QtWidgets.QLabel(self.frameCROSS)
        self.imageCROSS4.setGeometry(QtCore.QRect(210, 190, 180, 160))
        self.imageCROSS4.setObjectName("imageCROSS4")
        self.imageCROSS4.setPixmap(QtGui.QPixmap(overall_path + "\\cross4.png").scaled(180, 160))


        self.labelCross = QtWidgets.QLabel(Dialog)
        self.labelCross.setGeometry(QtCore.QRect(580, 770, 160, 20))
        self.labelCross.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCross.setObjectName("labelCross")


        self.framePARKING = QtWidgets.QFrame(Dialog)
        self.framePARKING.setGeometry(QtCore.QRect(10, 410, 400, 360))
        self.framePARKING.setMinimumSize(QtCore.QSize(400, 360))
        self.framePARKING.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePARKING.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePARKING.setObjectName("framePARKING")

        self.imagePARKING1 = QtWidgets.QLabel(self.framePARKING)
        self.imagePARKING1.setGeometry(QtCore.QRect(10, 10, 180, 160))
        self.imagePARKING1.setObjectName("imagePARKING1")
        self.imagePARKING1.setPixmap(QtGui.QPixmap(overall_path + "\\parking1.png").scaled(180, 160))

        self.imagePARKING2 = QtWidgets.QLabel(self.framePARKING)
        self.imagePARKING2.setGeometry(QtCore.QRect(10, 190, 180, 160))
        self.imagePARKING2.setObjectName("imagePARKING2")
        self.imagePARKING2.setPixmap(QtGui.QPixmap(overall_path + "\\parking2.png").scaled(180, 160))

        self.imagePARKING3 = QtWidgets.QLabel(self.framePARKING)
        self.imagePARKING3.setGeometry(QtCore.QRect(210, 10, 180, 160))
        self.imagePARKING3.setObjectName("imagePARKING3")
        self.imagePARKING3.setPixmap(QtGui.QPixmap(overall_path + "\\parking3.png").scaled(180, 160))

        self.imagePARKING4 = QtWidgets.QLabel(self.framePARKING)
        self.imagePARKING4.setGeometry(QtCore.QRect(210, 190, 180, 160))
        self.imagePARKING4.setObjectName("imagePARKING4")
        self.imagePARKING4.setPixmap(QtGui.QPixmap(overall_path + "\\parking4.png").scaled(180, 160))

        self.labelParking = QtWidgets.QLabel(Dialog)
        self.labelParking.setGeometry(QtCore.QRect(170, 770, 160, 20))
        self.labelParking.setAlignment(QtCore.Qt.AlignCenter)
        self.labelParking.setObjectName("labelParking")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ЗНАК СТОП"))
        self.labelSpeed.setText(_translate("Dialog", "ОГРАНИЧЕНИЕ СКОРОСТИ"))
        self.labelCross.setText(_translate("Dialog", "ПЕШЕХОДНЫЙ ПЕРЕХОД"))
        self.labelParking.setText(_translate("Dialog", "ПАРКОВКА ЗАПРЕЩЕНА"))
        self.labelDataSet.setText(_translate("Dialog", "Обучающий набор данных"))



class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)

        self.cwd = os.path.join(os.getcwd(), "modules", "DatasetPoisoning")
        self.changePicture(os.path.join(self.cwd, "pics", "speed3_atk.png"))

        self.showSlide()

    def executeAction(self, action):
        super().executeAction(action)
        if action.get("DialogWindow"):
            self.ExecuteDemoDialog(
                action["DialogWindow"]
            )
    
    def ExecuteDemoDialog(self, in_data : str):
        dialog_app = QtWidgets.QDialog()
        DialogWindow = SignDialog()
        DialogWindow.setupUi(dialog_app, self.cwd + "\\pics", in_data)
        dialog_app.exec()
    

    def showResult(self):
        if self.demonstration_type == "attack":
            self.ScriptTextPlate.insertPlainText("Знак Ограничение скорости")
            #self.changeScriptText("(Ограничение скорости)")
        else:
            self.ScriptTextPlate.insertPlainText("Знак Стоп")
            #self.changeScriptText("(Стоп)")
        