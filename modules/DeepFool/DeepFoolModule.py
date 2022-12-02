import os
import common.lib.SuperModule as SM
from PyQt5.QtWidgets import QComboBox

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
        self.parameters["param0"] += str(randint(1, 3))

        self.cwd = os.path.join("modules", "DeepFool")
        
        try:
            self.changePicture(os.path.join(self.cwd, "pics", self.parameters["param0"] + ".png"))
        except:
            self.changePicture(os.path.join(self.cwd, "pics", "мужчина1.png"))
        self.showSlide()
    

    def executeAction(self, action):
        super().executeAction(action)
        if action.get('Script'):
            self.ExecuteDemoScript(
                action['Script']
            )
    
    def ExecuteDemoScript(self, in_data : str):
        try:
            if noiseattack(os.path.join(self.cwd, "pics", self.parameters["param0"] + ".png"), level = in_data):
                self.changePicture(os.path.join(self.cwd, "pics", self.parameters["param0"] + "_out.png"))
        except:
            if noiseattack(os.path.join(self.cwd, "pics", "мужчина1.png"), level = "low"):
                self.changePicture(os.path.join(self.cwd, "pics", "мужчина1_out.png"))
    

    def showResult(self):
        if self.demonstration_type == "attack":
            if "мужчина" in self.parameters['param0']:
                text = "<br>[*] Man : 2%<p style='color:#FF0000';>[*] Woman : 97%</p>[*] Not Human : 1%<br>"
            else:
                text = "<br>[*] Woman : 2%<p style='color:#FF0000';>[*] Man : 97%</p>[*] Not Human : 1%<br>"
            #self.changeScriptText(text)
            self.ScriptTextPlate.insertHtml(text)


        else:
            if not ("мужчина" in self.parameters['param0']):
                text = "<br>[*] Man : 2%<p style='color:#00FF00';>[*] Woman : 97%</p>[*] Not Human : 1%<br>"
            else:
                text = "<br>[*] Woman : 2%<p style='color:#00FF00';>[*] Man : 97%</p>[*] Not Human : 1%<br>"
            #self.changeScriptText(text)
            self.ScriptTextPlate.insertHtml(text)

    def cleanup(self):
        for filename in os.listdir(os.path.join(self.cwd, "pics")):
            if "_out.png" in filename:
                os.remove(os.path.join(self.cwd, "pics", filename))
