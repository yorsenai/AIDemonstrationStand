import SuperModule as SM
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
		#new_name = image[7 : image.find(".p")]
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
        self.parameters["param0"]
        self.cwd = ".\\modules\\OnePixel\\"
        try:
            self.changePicture(self.cwd + "pics\\" + self.parameters["param0"] + ".png")
        except:
            self.changePicture(self.cwd + "pics\\собака.png")
        self.showSlide()
    

    def executeAction(self, action):
        super().executeAction(action)
        if action.get('Script'):
            self.ExecuteDemoScript(
                action['Script']
            )
    
    def ExecuteDemoScript(self, in_data : str):
        try:
            if onepixattack(self.cwd + "pics\\" + self.parameters["param0"] + ".png"):
                self.changePicture(self.cwd  + "pics\\" + self.parameters["param0"] + "_out.png")
        except:
            if onepixattack(self.cwd + "pics\\собака.png"):
                self.changePicture(self.cwd  + "pics\\собака_out.png")