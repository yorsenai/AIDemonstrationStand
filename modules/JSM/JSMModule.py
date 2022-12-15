import os
import common.lib.SuperModule as SM
from PyQt5.QtWidgets import QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets

from PIL import Image

def JSMattack(image : str):
	try:
		im = Image.open(image)
		pixelMap = im.load()
		
		img = Image.new( im.mode, im.size)
		pixelsNew = img.load()

		for i in range(img.size[0]):
			for j in range(img.size[1]):
				pixelsNew[i,j] = pixelMap[i,j]
		pixelsNew[11, 13] = (255,0,0,255)
		pixelsNew[13, 15] = (255,0,0,255)
		pixelsNew[15, 11] = (255,0,0,255)


		im.close()
		new_name = image.replace(".png", "")
		img.save(new_name + "_out.png", "PNG")
		img.close()

		return True
	except:
		return False





class BayesDialog(object):
    def setupUi(self, Dialog, overall_path : str):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 380)

        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setGeometry(QtCore.QRect(20, 5, 340, 30))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("label")
        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(12)
        self.labelImage.setFont(myFont)


        self.imageCNN = QtWidgets.QLabel(Dialog)
        self.imageCNN.setGeometry(QtCore.QRect(30, 40, 320, 320))
        self.imageCNN.setObjectName("imageBayes")        
        self.imageCNN.setPixmap(QtGui.QPixmap(os.path.join(overall_path, "Bayes.png")).scaled(320, 320))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelImage.setText(_translate("Dialog", "Формула условной вероятности"))


def addParams():
    values =  ["собака", "птица", "кошка", "лошадь"]
    combobox = QComboBox()
    combobox.addItems(values)
    return [combobox]

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)
        self.parameters["param1"]
        self.cwd = os.path.join("modules", "JSM")
        try:
            self.changePicture(os.path.join(self.cwd,  "pics", self.parameters["param1"] + ".png"))
        except:
            self.changePicture(os.path.join(self.cwd,  "pics", "собака.png"))
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
    
    def ExecuteDemoScript(self, _):
        try:
            if JSMattack(os.path.join(self.cwd,  "pics", self.parameters["param1"] + ".png")):
                self.changePicture(os.path.join(self.cwd,  "pics", self.parameters["param1"] + "_out.png"))
        except:
            if JSMattack(os.path.join(self.cwd,  "pics", "собака.png")):
                self.changePicture(os.path.join(self.cwd,  "pics", "собака_out.png"))
    
    def ExecuteDemoDialog(self, _):
        dialog_app = QtWidgets.QDialog()
        DialogWindow = BayesDialog()
        DialogWindow.setupUi(dialog_app, self.cwd + "\\pics")
        dialog_app.exec()
    
    def showResult(self):
        if self.demonstration_type == "attack":
            l = ["собака", "птица", "кошка", "лошадь"]
            l.remove(self.parameters['param1'])
            text = "<p style='color:#FF0000';>" + l[0] + "</p>"
            self.insertResultHtml(check = l[0], text = text)
        else:
            text = "<p style='color:#00FF00';>" + self.parameters['param1'] + "</p>"
            self.insertResultHtml(check = self.parameters['param1'], text = text)

    def cleanup(self):
        for filename in os.listdir(os.path.join(self.cwd, "pics")):
            if "_out.png" in filename:
                os.remove(os.path.join(self.cwd, "pics", filename))
