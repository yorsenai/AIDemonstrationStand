import common.lib.SuperModule as SM
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Module(SM.SuperModule):
    def __init__(self, demonstration_type : str, slides, parent = None, parameters = None) -> None:
        super().__init__(demonstration_type = demonstration_type, slides = slides, parent = parent, parameters = parameters)

        
        self.showSlide()

    def executeAction(self, action):
        super().executeAction(action)
        pass
    
    def ExecuteDemoDialog(self, in_data : str):
        pass
    

    def showResult(self):
        pass