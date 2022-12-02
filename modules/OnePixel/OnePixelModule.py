import os
import common.lib.SuperModule as SM
from PyQt5.QtWidgets import QComboBox

from PIL import Image
from random import randint

def onepixattack(image : str):
	try:
		im = Image.open(image)
		pixelMap = im.load()
		
		img = Image.new( im.mode, im.size)
		pixelsNew = img.load()

		for i in range(img.size[0]):
			for j in range(img.size[1]):
				pixelsNew[i,j] = pixelMap[i,j]
		pixelsNew[randint(10, 18), randint(10, 18)] = (255,0,0,255)


		im.close()
		new_name = image.replace(".png", "")
		img.save(new_name + "_out.png", "PNG")
		img.close()

		return True
	except:
		return False



def addParams():
    values =  ["собака", "птица", "кошка", "лошадь"]
    combobox = QComboBox()
    combobox.addItems(values)
    return [combobox]

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)
        self.parameters["param1"]
        self.cwd = os.path.join("modules", "OnePixel")
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
    
    def ExecuteDemoScript(self, in_data : str):
        try:
            if onepixattack(os.path.join(self.cwd,  "pics", self.parameters["param1"] + ".png")):
                self.changePicture(os.path.join(self.cwd,  "pics", self.parameters["param1"] + "_out.png"))
        except:
            if onepixattack(os.path.join(self.cwd,  "pics", "собака.png")):
                self.changePicture(os.path.join(self.cwd,  "pics", "собака_out.png"))
    
    def showResult(self):
        if self.demonstration_type == "attack":
            l = ["собака", "птица", "кошка", "лошадь"]
            l.remove(self.parameters['param1'])
            #self.changeScriptText("(" + l[0] + ")")
            self.ScriptTextPlate.insertPlainText(l[0])
        else:
            #self.changeScriptText(self.parameters['param1'])
            self.ScriptTextPlate.insertPlainText(self.parameters['param1'])

    def cleanup(self):
        for filename in os.listdir(os.path.join(self.cwd, "pics")):
            if "_out.png" in filename:
                os.remove(os.path.join(self.cwd, "pics", filename))
